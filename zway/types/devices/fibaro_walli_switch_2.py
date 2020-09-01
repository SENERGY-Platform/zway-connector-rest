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

__all__ = ('device_type_map', 'FibaroWalliSwitch2')

from ..service import GetEnergyConsumption_50_0, GetEnergyConsumption_50_0__1, GetEnergyConsumption_50_0__2, \
    GetOnOffState_37, GetOnOffState_37__1, GetOnOffState_37__2, GetPowerConsumption_50_2, GetPowerConsumption_50_2__1, \
    GetPowerConsumption_50_2__2, SetOffState_37, SetOffState_37__1, SetOffState_37__2, SetOnState_37, SetOnState_37__1, \
    SetOnState_37__2
from ..zway_device import ZwayDevice
from ...configuration import config


class FibaroWalliSwitch2(ZwayDevice):
    device_type_id = config.Senergy.dt_fibaro_walli_switch_2
    services = (GetEnergyConsumption_50_0, GetEnergyConsumption_50_0__1, GetEnergyConsumption_50_0__2,
                GetOnOffState_37, GetOnOffState_37__1, GetOnOffState_37__2, GetPowerConsumption_50_2,
                GetPowerConsumption_50_2__1,
                GetPowerConsumption_50_2__2, SetOffState_37, SetOffState_37__1, SetOffState_37__2, SetOnState_37,
                SetOnState_37__1,
                SetOnState_37__2)


device_type_map = {
    "fibaro_walli_switch_2": FibaroWalliSwitch2,
}
