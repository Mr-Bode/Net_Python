#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

print()

# start_time = datetime.now()
nexus1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

nexus2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

for switch in (nexus1, nexus2):
    connect_var = ConnectHandler(**switch)

    vlan_output = connect_var.send_config_from_file(config_file = "new_vlans.txt")
    print("#" * 80)
    print("vlan Changes: ")
    print(vlan_output)
    print("#" * 80)
    print()

    end_output = connect_var.save_config()
    print(end_output)

print()
connect_var.disconnect()
# end_time = datetime.now()
# print("Total Execution Time: {}\n".format(end_time - start_time))


