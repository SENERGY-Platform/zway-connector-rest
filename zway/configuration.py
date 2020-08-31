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

if not all((config.Senergy.dt_devolo_wall_plug, config.Senergy.dt_devolo_radiator_thermostat)):
    exit('Please provide a SENERGY device and service types')
