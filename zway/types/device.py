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

from .devices.devolo_wall_plug import DevoloWallPlug
from .devices.devolo_radiator_thermostat import DevoloRadiatorThermostat
from .devices.danfoss_radiator_thermostat import DanfossRadiatorThermostat
from .devices.aeotec_indoor_siren import AeotecIndoorSiren
from .devices.devolo_door_window_contact import DevoloDoorWindowContact
from .devices.aeotec_multisensor_gen_6 import AeotecMultiSensorGen6
from .devices.neo_coolcam_d_w_sensor import NeoCoolcamDWSensor
from .devices.abus_led_light_SHLM10010 import AbusLedLightSHLM10010
from .devices.neo_coolcam_multisensor import NeoCoolcamMultiSensor
from .devices.cyrus_4in1_multisensor import Cyrus4in1Multisensor
from .devices.fibaro_wall_plug_FGWPx102ZW5 import FibaroWallPlugFGWPx102ZW5
from .devices.fibaro_pir_g5 import FibaroPirG5
from .devices.fibaro_the_button import FibaroTheButton
from .devices.aeotec_door_window_sensor_7 import AeotecDoorWindowSensor7
from .devices.fibaro_walli_switch_2 import FibaroWalliSwitch2

__all__ = ('get_device_class', 'UnknownDeviceTypeError')

type_map = {
    "373-1-18": DevoloWallPlug,
    "2-5-373": DevoloRadiatorThermostat,
    "2-5-4": DanfossRadiatorThermostat,
    "134-4-80": AeotecIndoorSiren,
    "373-2-14": DevoloDoorWindowContact,
    "134-2-100": AeotecMultiSensorGen6,
    "600-3-4226": NeoCoolcamDWSensor,
    "1027-3-2": AbusLedLightSHLM10010,
    "600-3-4237": NeoCoolcamMultiSensor,
    "265-8225-8449": Cyrus4in1Multisensor,
    "271-1538-4097": FibaroWallPlugFGWPx102ZW5,
    "271-2049-4097": FibaroPirG5,
    "271-3841-4096": FibaroTheButton,
    "881-2-7": AeotecDoorWindowSensor7,
    "271-6913-4096": FibaroWalliSwitch2,
}


class UnknownDeviceTypeError(BaseException):
    """Indicates that the request combination of manufacturer_id, manufacturer_product_type and manufacturer_product_id
    is not known"""
    pass


def get_device_class(manufacturer_id: int, manufacturer_product_type: int, manufacturer_product_id):
    """Returns the matching device class or raises an UnknownDeviceTypeError"""
    key = str(manufacturer_id) + '-' + str(manufacturer_product_type) + '-' + str(manufacturer_product_id)
    if key not in type_map:
        raise UnknownDeviceTypeError
    return type_map[key]
