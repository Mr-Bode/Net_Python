#!/usr/bin/env python

import yaml
from pprint import pprint

cisco_nx1 = {"device_name": "nxos1", "host": "nxos1.lasthop.io", "username": "admin", "password": "cisco321"}

cisco_nx2 = {"device_name": "nx02", "host": "nxos2.lasthop.io", "username": "admin", "password": "cisco321"}

arista1 = {"device_name": "arista1", "host": "arista1.lasthop.io", "username": "admin", "password": "cisco321"}

arista2 = {"device_name": "arista2", "host": "arista2.lasthop.io", "username": "admin", "password": "cisco321"}

my_devices = [cisco_nx1, cisco_nx2, arista1, arista2]

print()
pprint(my_devices)
print()


with open("my_devices.yml", "w") as new_yaml:
    yaml.dump(my_devices, new_yaml, default_flow_style=False)