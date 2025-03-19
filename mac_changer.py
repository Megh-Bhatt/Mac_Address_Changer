#!/usr/bin/env python

import subprocess
import optparse
import re
def mac_changer(interface,mac_address):
    result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)
    output = result.stdout
    cur_mac = re.search(r"(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})", output)
    if cur_mac:
        print("Current Mac address for " + interface + " is " + cur_mac.group(1))
    else:
        print("[-] Could not read mac address")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])
    print("Mac address changes successfully")
    result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)
    output = result.stdout
    cur_mac = re.search(r"(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})", output)
    if cur_mac:
        print("New Current Mac address for " + interface + " is " + cur_mac.group(1))
    else:
        print("[-] Could not read mac address")
def get_values():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",help="Enter the Interface you want to change mac address for")
    parser.add_option("-m", "--mac", dest="mac", help="Enter the mac address you want the Interface to change to")
    (values,arguments)=parser.parse_args()
    if not values.interface:
        parser.error("Please input interface for which the mac is to be changed, for more info use --help option")
    if not values.mac:
        parser.error("Please input the new mac address, for more info use --help option")
    return values
values=get_values()
mac_changer(values.interface,values.mac)



