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

from simple_conf import configuration, section
from os import getcwd, makedirs
from os.path import exists as path_exists

user_dir = '{}/storage'.format(getcwd())


@configuration
class ZwayConf:
    @section
    class Zway:
        url = "http://localhost:8083"
        username = ""
        password = ""

    @section
    class Senergy:
        dt_devolo_wall_plug = "urn:infai:ses:device-type:1c200f02-67ac-42e1-8c6c-748bdc091764"
        dt_devolo_radiator_thermostat = "urn:infai:ses:device-type:9ae1f9eb-ebd6-4fb5-ae1f-a03d40c500ed"
        dt_danfoss_radiator_thermostat = "urn:infai:ses:device-type:662d9c9f-949d-4577-9485-9cb7255f547f"
        dt_aeotec_indoor_siren = "urn:infai:ses:device-type:6c05a263-7318-47bf-a4af-a0d13cc95008"
        dt_devolo_door_window_contact = "urn:infai:ses:device-type:d4219e84-d14b-42be-9cd8-1afe4fd2afe5"
        dt_aeotec_multisensor_gen_6 = "urn:infai:ses:device-type:39d1e71a-a5d2-4471-b251-466f60c7d398"
        dt_neo_coolcam_d_w_sensor = "urn:infai:ses:device-type:052d6e99-32f4-483f-967e-16341127ff89"
        dt_abus_led_light_SHLM10010 = "urn:infai:ses:device-type:af2a302f-51c7-4344-a8fc-894cfaebb1bd"
        dt_neo_coolcam_multisensor = "urn:infai:ses:device-type:bec7e624-9a65-4a50-ab3d-d3fd8ce4bfe1"

    @section
    class Logger:
        level = "info"

    @section
    class Controller:
        max_command_age = 180

    @section
    class RuntimeEnv:
        max_start_delay = 30


if not path_exists(user_dir):
    makedirs(user_dir)

config = ZwayConf('zway.conf', user_dir)

if not all((config.Zway.url, config.Zway.username, config.Zway.password)):
    exit('Please provide zway information')

if not all((config.Senergy.dt_devolo_wall_plug, config.Senergy.dt_devolo_radiator_thermostat,
            config.Senergy.dt_danfoss_radiator_thermostat, config.Senergy.dt_aeotec_indoor_siren,
            config.Senergy.dt_devolo_door_window_contact, config.Senergy.dt_aeotec_multisensor_gen_6,
            config.Senergy.dt_neo_coolcam_d_w_sensor, config.Senergy.dt_abus_led_light_SHLM10010,
            config.Senergy.dt_neo_coolcam_multisensor)):
    exit('Please provide a SENERGY device types')
