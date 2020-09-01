"""
   Copyright 2020 InfAI (CC SES)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import datetime
import time
from typing import List, Dict
from os import sep
from json import dump

import requests
from cc_lib._configuration.configuration import cc_conf
from cc_lib.types import Device

from .configuration import config
from .logger import root_logger
from .types.device import get_device_class, UnknownDeviceTypeError

logger = root_logger.getChild(__name__.split(".", 1)[-1])

api_prefix_vdev = '/ZAutomation/api/v1/'
api_prefix_zwave = '/ZWave.zway/Data/'
endpoints = {"login": config.Zway.url + api_prefix_vdev + 'login',
             "status": config.Zway.url + api_prefix_vdev + 'status',
             "vdevs": config.Zway.url + api_prefix_vdev + 'devices', "zwave": config.Zway.url + api_prefix_zwave,
             "zwave_cmd": config.Zway.url + '/ZWave.zway/Run/'}

http_timeout = 2


class Zway():
    def __init__(self):
        self.auth_header = None
        self.ensure_login()
        self.__get_uuid()

    def ensure_login(self):
        """Makes sure the login is still valid. Blocks until logged in successfully"""
        r = requests.get(endpoints["status"], headers=self.auth_header,
                         timeout=http_timeout)
        if not r.ok:
            logger.info('Renewing Zway login')
            sleep = 2
            while not self.login():
                logger.info("retry login in " + str(sleep) + " seconds...")
                time.sleep(sleep)
                sleep += 2
        else:
            logger.debug('Still logged in at Zway')

    def login(self) -> bool:
        """Logs in at Zway with pre-configured credentials. Return True if login was successful"""
        r = requests.post(endpoints["login"], data={'login': config.Zway.username, 'password': config.Zway.password},
                          timeout=http_timeout)
        resp = r.json()
        if resp["code"] != 200:
            logger.error('Could not login: ' + resp["message"])
            return False
        self.auth_header = {'ZWAYSession': resp["data"]["sid"]}
        logger.info('Logged in at Zway as ' + resp["data"]["name"])
        return True

    def get_devices(self, since: int = 0) -> List[Device]:
        """Returns all devices registered at zway and converts them to platform devices. If needed, supply a unix timestamp and only receive devices that
        have been added since"""
        zway_devices = self.get_physical_devices(since)
        platform_devices = []

        for id, zway_device in zway_devices.items():
            try:
                platform_devices.append(
                    get_device_class(zway_device['data']['manufacturerId']['value'],
                                     zway_device['data']['manufacturerProductType']['value'],
                                     zway_device['data']['manufacturerProductId']['value'])
                    (id, zway_device['data']['givenName']['value'] + '(#' + id + ')',
                     {"connected": not zway_device['data']['isFailed']['value']}))
            except UnknownDeviceTypeError:
                logger.error("Unknown device detected")
                path = 'storage' + sep + id + '.json'
                with open(path, 'w') as f:
                    dump(zway_device, f, indent=4)
                    logger.info("Device info written to " + path)

        return platform_devices

    def get_physical_devices(self, since: int = 0) -> Dict:
        self.ensure_login()
        r = requests.post(endpoints["zwave"] + str(since), headers=self.auth_header, timeout=http_timeout)
        if not r.ok:
            logger.error('Could not get devices from zway, received code ' + str(r.status_code))
            return {}
        return r.json()["devices"]

    @property
    def uuid(self) -> str:
        if cc_conf.device.id_prefix is not None:
            return cc_conf.device.id_prefix
        return self.__get_uuid()

    def __get_uuid(self):
        self.ensure_login()
        r = requests.post(endpoints["zwave"] + '0', headers=self.auth_header, timeout=http_timeout)
        if not r.ok:
            logger.error('Could not get devices from zway, received code ' + str(r.status_code))
            return ''
        resp = r.json()
        uuid = resp["controller"]["data"]["uuid"]["value"]
        cc_conf.device.id_prefix = uuid
        return uuid

    def run_control_cmd(self, id: str, instance: str, cmd_class: str, value: str, subsection: str = None):
        self.ensure_login()
        url = endpoints["zwave_cmd"] + 'devices[' + id + '].instances[' + instance \
              + '].commandClasses[' + cmd_class + '].Set( '
        if subsection is not None:
            url += subsection + ','
        url += value + ')'

        r = requests.post(url, headers=self.auth_header, timeout=http_timeout)
        if not r.ok:
            logger.error('Could not run zway control command, received code ' + str(r.status_code))
            return
        logger.debug('Zway Command response code: ' + str(r.status_code))

    def run_measuring_cmd(self, id: str, instance: str, cmd_class: str, subsection: str = None) -> Dict:
        url = endpoints["vdevs"] + '/ZWayVDev_zway_' + id + '-' + instance + '-' + cmd_class
        if subsection is not None:
            url += '-' + subsection
        logger.debug("Trying to get data from zway url: " + url)
        r = requests.get(url, headers=self.auth_header, timeout=http_timeout)
        if not r.ok:
            logger.error('Could not run zway measuring command, received code ' + str(r.status_code))
            return {}
        resp = r.json()
        iso_time = datetime.datetime.utcfromtimestamp(resp["data"]["updateTime"]).isoformat() + 'Z'
        return {"level": resp["data"]["metrics"]["level"], "updateTime": iso_time}
