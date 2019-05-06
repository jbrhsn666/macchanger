#! /usr/bin/env python
import re
import subprocess


class MacChanger:
    # Class containing mac changer functions
    def __init__(self, iface, new_mac):
        self.iface = iface
        self.new_mac = new_mac
        self.changemac()

    def changemac(self):
        # Changing Mac To New MAC
        print("\n[+]Trying to change MAC address\n\n")
        subprocess.call(["ifconfig", self.iface, "down"])
        subprocess.call(["ifconfig", self.iface, "hw", "ether", self.new_mac])
        subprocess.call(["ifconfig", self.iface, "up"])
        self.checkmac()

    def checkmac(self):
        # Checking Changed MAC
        print("\n[+] Checking for the changed MAC\n\n")
        result = subprocess.check_output(["ifconfig", self.iface])
        changed_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))
        if changed_mac.group(0) == self.new_mac:
            print("\n[+] MAC address of " + self.iface + " successfully changed to " + self.new_mac + "\n")
