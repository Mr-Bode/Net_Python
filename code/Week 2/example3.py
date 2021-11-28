#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

router = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    
}

connector = ConnectHandler(**router)

print()
command_query = ["show version", "show lldp neighbors"]

for query in command_query:
    output = connector.send_command(query, use_textfsm=True)
    print("#" * 80)
    print(query)
    print("#" * 80)
    pprint(output)
    print("#" * 80)
    print()

connector.disconnect()