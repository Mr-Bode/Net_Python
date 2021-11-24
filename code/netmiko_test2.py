#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

nexus1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
}

nexus2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
}

for switch in (nexus1, nexus2):
    switch_connect = ConnectHandler(**switch)
    print(switch_connect.find_prompt())
