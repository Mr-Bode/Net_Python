#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "session_log": "my_output.txt",
}

cisco_connect = ConnectHandler(**device)
print("\nCurrent Prompt: ")
print(cisco_connect.find_prompt())

print("\nEnter Config mode - current prompt: ")
cisco_connect.config_mode()
print(cisco_connect.find_prompt())

print("\nExit Config mode - current prompt: ")
cisco_connect.exit_config_mode()
print(cisco_connect.find_prompt())

print("\nExit privileged exec (disable), Current Prompt: ")
cisco_connect.write_channel("disable\n")
#time.sleep(2)
output = cisco_connect.read_channel()
print(output)

print("\nRe-enter enable mode, Current Prompt: ")
cisco_connect.enable()
print(cisco_connect.find_prompt())

cisco_connect.disconnect()
print()