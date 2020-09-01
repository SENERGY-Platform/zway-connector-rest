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

__all__ = (
    'GetEnergyConsumption_50_0', 'GetOnOffState_37', 'GetPowerConsumption_50_2', 'SetOnState_37', 'SetOffState_37',
    'GetBatteryState_128', 'GetTargetTemperature_67_1', 'GetTemperature_49_1', 'SetTargetTemperature_67_1',
    'GetHumidity_49_5', 'GetLuminiscence_49_3', 'GetMotionState_48_1', 'GetTamperState_113_7_3_A',
    'GetUltraviolet_49_27', 'GetOnOffState_48_10', 'GetTamperState_48_8', 'SetOffState_38', 'SetOnState_38',
    'GetMotionState_48_12', 'GetTamperState_113_7_8_A', 'GetPowerConsumption_49_4', 'GetToggleState_0_1_S',
    'SetToggle_0_1_S', 'GetOnOffState_113_6_Door_A', 'GetTiltState_48_11', 'GetEnergyConsumption_50_0__1',
    'GetEnergyConsumption_50_0__2', 'GetOnOffState_37__1', 'GetOnOffState_37__2', 'GetPowerConsumption_50_2__1',
    'GetPowerConsumption_50_2__2', 'SetOnState_37__1', 'SetOnState_37__2', 'SetOffState_37__1', 'SetOffState_37__2',
    'GetAlarm_13_3_1_A', 'GetCarbonDioxid_49_17')

import cc_lib
from cc_lib.types import Device

from ..logger import root_logger

logger = root_logger.getChild(__name__.split(".", 1)[-1])

converter_pool = dict()


class GetEnergyConsumption_50_0(cc_lib.types.Service):
    local_id = "get_level:50-0"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '50', '0')


class GetEnergyConsumption_50_0__1(cc_lib.types.Service):
    local_id = "get_level:50-0:1"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '1', '50', '0')


class GetEnergyConsumption_50_0__2(cc_lib.types.Service):
    local_id = "get_level:50-0:2"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '2', '50', '0')


class GetOnOffState_37(cc_lib.types.Service):
    local_id = "get_level:37"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '37')


class GetOnOffState_37__1(cc_lib.types.Service):
    local_id = "get_level:37:1"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '1', '37')


class GetOnOffState_37__2(cc_lib.types.Service):
    local_id = "get_level:37:2"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '2', '37')


class GetOnOffState_48_10(cc_lib.types.Service):
    local_id = "get_level:48-10"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '48', '10')


class GetPowerConsumption_50_2(cc_lib.types.Service):
    local_id = "get_level:50-2"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '50', '2')


class GetPowerConsumption_50_2__1(cc_lib.types.Service):
    local_id = "get_level:50-2:1"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '1', '50', '2')


class GetPowerConsumption_50_2__2(cc_lib.types.Service):
    local_id = "get_level:50-2:2"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '2', '50', '2')


class SetOnState_37(cc_lib.types.Service):
    local_id = "on:37"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_control_cmd(device.id, '0', '37', '255')


class SetOnState_37__1(cc_lib.types.Service):
    local_id = "on:37:1"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_control_cmd(device.id, '1', '37', '255')


class SetOnState_37__2(cc_lib.types.Service):
    local_id = "on:37:2"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_control_cmd(device.id, '2', '37', '255')


class SetOnState_38(cc_lib.types.Service):
    local_id = "on:38"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_control_cmd(device.id, '0', '37', '255')


class SetOffState_37(cc_lib.types.Service):
    local_id = "off:37"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_control_cmd(device.id, '0', '37', '0')


class SetOffState_37__1(cc_lib.types.Service):
    local_id = "off:37__1"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_control_cmd(device.id, '1', '37', '0')


class SetOffState_37__2(cc_lib.types.Service):
    local_id = "off:37:2"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_control_cmd(device.id, '2', '37', '0')


class SetOffState_38(cc_lib.types.Service):
    local_id = "off:38"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_control_cmd(device.id, '0', '38', '0')


class GetBatteryState_128(cc_lib.types.Service):
    local_id = "get_level:128"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '128')


class GetTargetTemperature_67_1(cc_lib.types.Service):
    local_id = "get_level:67-1"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '67', '1')


class GetTemperature_49_1(cc_lib.types.Service):
    local_id = "get_level:49-1"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '49', '1')


class SetTargetTemperature_67_1(cc_lib.types.Service):
    local_id = "exact:67-1"

    @staticmethod
    def task(device: Device, zway, level):
        return zway.run_control_cmd(device.id, '0', '67', str(level), '1')


class GetTamperState_48_8(cc_lib.types.Service):
    local_id = "get_level:48-8"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '48', '8')


class GetHumidity_49_5():
    local_id = "get_level:49-5"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '49', '5')


class GetLuminiscence_49_3():
    local_id = "get_level:49-3"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '49', '3')


class GetMotionState_48_1():
    local_id = "get_level:48-1"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '48', '1')


class GetTamperState_113_7_3_A():
    local_id = "get_level:113-7-3-A"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '113', '7-3-A')


class GetUltraviolet_49_27():
    local_id = "get_level:49-27"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '49', '27')


class GetMotionState_48_12():
    local_id = "get_level:48-12"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '48', '12')


class GetTamperState_113_7_8_A():
    local_id = "get_level:113-7-8-A"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '113', '7-8-A')


class GetPowerConsumption_49_4():
    local_id = "get_level:49-4"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '49', '4')


class GetToggleState_0_1_S():
    local_id = "get_level:0-1-S"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '0', '1-S')


class SetToggle_0_1_S():
    local_id = "on:0-1-S"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_control_cmd(device.id, '0', '0', '255', '1-S')


class GetOnOffState_113_6_Door_A():
    local_id = "get_level:113-6-Door-A"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '113', '6-Door-A')


class GetTiltState_48_11():
    local_id = "get_level:48-11"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '48', '11')


class GetAlarm_13_3_1_A():
    local_id = "get_level:113-3-1-A"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '113', '3-1-A')


class GetCarbonDioxid_49_17():
    local_id = "get_level:49-17"

    @staticmethod
    def task(device: Device, zway):
        return zway.run_measuring_cmd(device.id, '0', '49', '17')
