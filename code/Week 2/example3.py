#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

router = {
<<<<<<< HEAD
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
=======
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
>>>>>>> abe3321dee41c36c2ebf7663c704ccb542d8a066
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

<<<<<<< HEAD
    if query == "show lldp neighbors":
        print("LLDP Data Structure Type: {}".format(type(output)))
        print("HPE Switch Connection Port: {}".format(output[0]["neighbor_interface"]))

=======
>>>>>>> abe3321dee41c36c2ebf7663c704ccb542d8a066
connector.disconnect()