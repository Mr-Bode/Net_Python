#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

start_time = datetime.now()
cisco_router = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "fast_cli": True,
}

connect_var = ConnectHandler(**cisco_router)

print()
comms = [
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup"
]


dns_output = connect_var.send_config_set(comms)
print("#" * 80)
print("Config Change: ")
print(dns_output)
print("#" * 80)
print()

ping_output = connect_var.send_command("ping google.co.uk")
if "!!" in ping_output:
    print("Ping Successful: \n")
    print(ping_output)
else:
    print("Can't Ping site!")

print()
end_time = datetime.now()
print("Total Execution Time: {}\n".format(end_time - start_time))


