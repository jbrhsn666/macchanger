#! /usr/bin/env python

import argparse
import subprocess
import re
import macchangerclass


def showinterfaces():
    # Listing the available interfaces
    result = subprocess.check_output(["ifconfig"])
    interfaces = re.findall(r"(.*)(?:\s*Link\sencap)", result)
    print ("\n[+] Prompt Mode\n\n[+] Available network interfaces in your device\n")
    for interface in interfaces:
        if "lo" not in interface:
            print ("  {*} " + interface + "\n")
        else:
            print ("  {*} " + interface + " -> [!!] May be a loopback device \n")


def getinput():
    # Get inputs through prompt
    showinterfaces()
    interface = raw_input("[*] Enter interface to change MAC\n\n\t")
    new_mac = raw_input("\n[*] Enter new MAC address. Eg:- ff:ff:ff:ff:ff:ff\n\n\t")
    macchangerclass.MacChanger(interface, new_mac)


def parseargs():
    # Setting command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Enter the interface name")
    parser.add_argument("-m", "--mac", dest="new_mac", help="Enter new MAC address Eg:- ff:ff:ff:ff:ff:ff")
    args = parser.parse_args()
    print("\n[+] Commandline Usage --> macchanger.py [-h] [-i INTERFACE] [-m NEW_MAC]\n")
    if not args.interface and not args.new_mac:
        getinput()
    elif args.interface and args.new_mac:
        macchangerclass.MacChanger(args.interface, args.new_mac)
    else:
        print()
        print("\n[!] You haven't entered either interface or mac\n\n"
              "[-] Switching into prompt mode\n")
        getinput()


def startfn():
    # Starting Function to implement Exception Handling
    try:
        print("\n*************************************************")
        print("*\t\t\t\t\t\t*\n*\t\tMAC Address Changer\t\t*\n*\t\t\t\t\t\t*")
        print("*\t\t\t\t\t\t*\n*\t\tby @jbrhsn\t\t\t*\n*\t\t\t\t\t\t*")
        print("*************************************************\n")
        parseargs()
    except Exception, e:
        print("\r\n[-] Something Went Wrong ..! Exiting program..!!\n\n")
        exit(0)
    except KeyboardInterrupt, e:
        print("\r\n[-] User exited program...! Exiting..!!!\n\n")
        exit(0)


startfn()
