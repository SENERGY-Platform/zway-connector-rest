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

__all__ = ('GetEnergyConsumption', 'GetOnOffState', 'GetPowerConsumption', 'SetOnState', 'SetOffState',
           'GetBatteryState', 'GetTargetTemperature', 'GetTemperature', 'SetTargetTemperature')

import cc_lib
from cc_lib.types import Device

from ..logger import root_logger

logger = root_logger.getChild(__name__.split(".", 1)[-1])

converter_pool = dict()


class GetEnergyConsumption(cc_lib.types.Service):
    local_id = "get_level:50-0"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '50', '0')


class GetOnOffState(cc_lib.types.Service):
    local_id = "get_level:37"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '37')


class GetPowerConsumption(cc_lib.types.Service):
    local_id = "get_level:50-2"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '50', '2')


class SetOnState(cc_lib.types.Service):
    local_id = "on:37"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_control_cmd(device.id, '0', '37', '255')


class SetOffState(cc_lib.types.Service):
    local_id = "off:37"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_control_cmd(device.id, '0', '37', '0')


class GetBatteryState(cc_lib.types.Service):
    local_id = "get_level:128"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '128')


class GetTargetTemperature(cc_lib.types.Service):
    local_id = "get_level:67-1"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '67', '1')


class GetTemperature(cc_lib.types.Service):
    local_id = "get_level:49-1"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '49', '1')


class SetTargetTemperature(cc_lib.types.Service):
    local_id = "exact:67-1"

    @staticmethod
    def task(device: Device, zway, level):
        return zway.run_control_cmd(device.id, '0', '67', str(level), '1')

