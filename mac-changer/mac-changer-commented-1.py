#!usr/bin/env python

import subprocess # input commands in cmd
import time # set time
import optparse # parse arguments to the script on cmd
import re # use regex

def get_arguments():
    # create the function get_arguments
    parser = optparse.OptionParser()
    # assign the function OptionParser from the module optparse to the variable parser
    parser.add_option("-i", "--interface", dest="interface", help="Choose interface.")
    parser.add_option("-m", "--mac", dest="new_mac", help="Choose new MAC address.")
    # add the arguments to be used
    (options, arguments) = parser.parse_args()
    # parse the arguments to the variables options and arguments
    if not options.interface:
        # create a conditional to check if the user didnt input the options argument for interface
        parser.error("Please specify an interface, type --help for help")
    elif not options.new_mac:
        # create a conditional to check if the user didnt input the options argument for new_mac
        parser.error("Please specify a new MAC address, type --help for help")
    return options
    # return the values stored in options

def change_mac(interface, new_mac):
    # create the function change_mac
    print("[+] Change inferface " + interface + " to " + new_mac + " [+]")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    # use the subprocess module to call the commands to execute
    print("[+] Applying changes... [+]")
    time.sleep(1)

def get_current_mac(interface):
    # create function get_current_mac
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # use the check_output function of the subprocess module to check the MAC address and assign it to ifconfig_result
    mac_sr = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    # assign the values of the regex search in ifconfig_result to the variable mac_sr
    if mac_sr:
        # check if the interface has MAC address, if not print an error
        return (mac_sr.group(0))
    else:
        print("[-] Could not find MAC address [-]")

options = get_arguments()
# assing the function get_arguments to the options variable

current_mac = get_current_mac(options.interface)
# assign the values of the get_current_mac function to the current_mac variable

print("[+] Current MAC = " + str(current_mac) + " [+]")
# print current mac

change_mac(options.interface, options.new_mac)
# call function change_mac and change the mac address of the selected interface (stored in options)

current_mac = get_current_mac(options.interface)
# assing the changed mac address to the variable current_mac again (=new mac)

if current_mac == options.new_mac:
    # if the current_mac is equal to the mac parsed with the argument: print a successfull message
    print("[+] MAC address successfully changed to " + current_mac + " [+]")
else:
    # if not print an error
    print("[+] ERROR! MAC address was not changed [+]")

#Example: python3 mac-changer.py -i eth0 -m 00:11:22:33:44:55