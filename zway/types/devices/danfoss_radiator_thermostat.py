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


from ..service import GetBatteryState, GetTargetTemperature, SetTargetTemperature
from threading import Lock
from ...configuration import config
import cc_lib


class DanfossRadiatorThermostat(cc_lib.types.Device):
    device_type_id = config.Senergy.dt_danfoss_radiator_thermostat
    services = (GetBatteryState, GetTargetTemperature, SetTargetTemperature)

    def __init__(self, id: str, name: str, state: dict):
        self.id = id
        self.name = name
        self.__state_lock = Lock()
        self.state = state

    @property
    def state(self):
        with self.__state_lock:
            return self.__state

    @state.setter
    def state(self, arg):
        with self.__state_lock:
            self.__state = arg

    def getService(self, srv_handler: str, *args, **kwargs):
        service = super().getService(srv_handler)
        return service.task(self, *args, **kwargs)

    def __iter__(self):
        items = (
            ("name", self.name),
            ("state", self.state)
        )
        for item in items:
            yield item


device_type_map = {
    "danfoss_radiator_thermostat": DanfossRadiatorThermostat,
}
