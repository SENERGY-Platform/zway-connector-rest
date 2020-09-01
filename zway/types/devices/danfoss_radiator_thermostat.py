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

__all__ = ('device_type_map', 'DanfossRadiatorThermostat')

from ..service import GetBatteryState_128, GetTargetTemperature_67_1, SetTargetTemperature_67_1
from ..zway_device import ZwayDevice
from ...configuration import config


class DanfossRadiatorThermostat(ZwayDevice):
    device_type_id = config.Senergy.dt_danfoss_radiator_thermostat
    services = (GetBatteryState_128, GetTargetTemperature_67_1, SetTargetTemperature_67_1)


device_type_map = {
    "danfoss_radiator_thermostat": DanfossRadiatorThermostat,
}
