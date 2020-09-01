"""
   Copyright 2019 InfAI (CC SES)

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
import random
import time

import cc_lib
from cc_lib.client import DeviceAddError

from zway.configuration import config
from zway.controller import Controller
# from zway.monitor import Monitor
from zway.device_manager import DeviceManager
from zway.logger import root_logger
from zway.zway import Zway

logger = root_logger.getChild(__name__.split(".", 1)[-1])

if config.RuntimeEnv.max_start_delay > 0:
    delay = random.randint(1, config.RuntimeEnv.max_start_delay)
    print("delaying start for {}s".format(delay))
    time.sleep(delay)


def on_connect(client: cc_lib.client.Client):
    devices = device_manager.devices
    for device in devices.values():
        try:
            client.addDevice(device)  # TODO: differentiate adding/connecting
        except DeviceAddError:
            logger.error("Device probably exists already")
        if device.state["connected"]:
            try:
                client.connectDevice(device)
            except cc_lib.client.DeviceConnectError:
                pass
        else:
            logger.info("Skipping device " + device.id + ", Reason: Offline")
    connector_client.syncHub(list(devices.values()))


connector_client = cc_lib.client.Client()
connector_client.setConnectClbk(on_connect)

zway = Zway()
device_manager = DeviceManager(zway)

# cloud_monitor = Monitor(device_manager, connector_client)
controller = Controller(device_manager, connector_client, zway)

if __name__ == '__main__':
    while True:
        try:
            connector_client.initHub()
            break
        except cc_lib.client.HubInitializationError:
            time.sleep(10)

    connector_client.connect(reconnect=True)

    # cloud_monitor.start()
    controller.start()
    try:
        # cloud_monitor.join()
        controller.join()
    except KeyboardInterrupt:
        print("\ninterrupted by user\n")
