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

__all__ = ('device_type_map', 'FibaroWallPlugFGWPx102ZW5')

from ..service import GetEnergyConsumption_50_0, GetOnOffState_37, GetPowerConsumption_49_4, GetPowerConsumption_50_2, \
    SetOnState_37, SetOffState_37
from ..zway_device import ZwayDevice
from ...configuration import config


class FibaroWallPlugFGWPx102ZW5(ZwayDevice):
    device_type_id = config.Senergy.dt_fibaro_wall_plug_FGWPx102ZW5
    services = (
        GetEnergyConsumption_50_0, GetOnOffState_37, GetPowerConsumption_49_4, GetPowerConsumption_50_2, SetOnState_37,
        SetOffState_37)


device_type_map = {
    "fibaro_wall_plug_FGWPx102ZW5": FibaroWallPlugFGWPx102ZW5,
}
