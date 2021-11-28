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

ping_output = router_connect.send_command(
    command, expect_string=r"Protocol", strip_prompt=False, strip_command=False
)
ping_output += router_connect.send_command(
    "\n", expect_string=r"Target IP address", strip_prompt=False, strip_command=False
    )
ping_output += router_connect.send_command(
    "8.8.8.8", expect_string=r"Repeat count", strip_prompt=False, strip_command=False
)
ping_output += router_connect.send_command(
    "\n", expect_string=r"Datagram size", strip_prompt=False, strip_command=False
    )
ping_output += router_connect.send_command(
    "\n", expect_string=r"Timeout in seconds", strip_prompt=False, strip_command=False
    )
ping_output += router_connect.send_command(
    "\n", expect_string=r"Extended commands", strip_prompt=False, strip_command=False
    )
ping_output += router_connect.send_command(
    "\n", expect_string=r"Sweep range of sizes", strip_prompt=False, strip_command=False
    )
ping_output += router_connect.send_command(
    "\n", expect_string=r"#", strip_prompt=False, strip_command=False
    )

router_connect.disconnect()

print("\n")
print(ping_output)
