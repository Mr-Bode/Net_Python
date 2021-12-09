#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

cisco4 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass()
    }

router_connect = ConnectHandler(**cisco4)
print(f"Here's the prompt: {router_connect.find_prompt()}")

command = "ping"
ping_output = router_connect.send_command_timing(
    command, strip_prompt=False, strip_command=False
    )
ping_output += router_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
ping_output += router_connect.send_command_timing(
    "8.8.8.8", strip_prompt=False, strip_command=False
)
ping_output += router_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
ping_output += router_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
ping_output += router_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
ping_output += router_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
ping_output += router_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)

router_connect.disconnect()

print("\n")
print(ping_output)
