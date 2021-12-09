#!/usr/bin/env python

import re
from pprint import pprint

arp_table = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

arp_table = arp_table.strip()
# Convert to a list
arp_list = arp_table.splitlines()
# print(arp_list[4])

final_list = []

for arp_entry in arp_list:
    if re.search(r"^Protocol.*Interface", arp_entry):
        continue
    _, ip_addr, _, mac_addr, _, interface = arp_entry.split()
    arp_dict = {"mac": mac_addr, "ip": ip_addr, "interface": interface}
    final_list.append(arp_dict)

print()
print(final_list)
print() 