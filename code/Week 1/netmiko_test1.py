#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

connection_netz = ConnectHandler(
    host='nxos2.lasthop.io',
    username='pyclass',
    password=getpass(),
    device_type='cisco_nxos',
)

print(connection_netz.find_prompt())
