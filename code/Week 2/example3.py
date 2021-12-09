#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

router = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
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

    if query == "show lldp neighbors":
        print("LLDP Data Structure Type: {}".format(type(output)))
        print("HPE Switch Connection Port: {}".format(output[0]["neighbor_interface"]))

connector.disconnect()