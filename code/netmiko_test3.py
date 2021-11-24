#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

cisco3 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
}

switch_connect = ConnectHandler(**cisco3)
output = switch_connect.send_command("show version")

with open("show_version.txt", "w") as logs:
    logs.write(output)

switch_connect.disconnect()
