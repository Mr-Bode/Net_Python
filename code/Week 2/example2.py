#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

nexus = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "global_delay_factor": 2,
}

connectz = ConnectHandler(**nexus)

command = "show lldp neighbors detail"

output = connectz.send_command(command)

print("#" * 80)
print(output)
print("#" * 80)


another_output = connectz.send_command(command, delay_factor=8)
connectz.disconnect()

print("#" * 80)
print(another_output)
print("#" * 80)