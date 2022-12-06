import subprocess
from optparse import OptionParser
import re

def get_args():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address") 
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address") 
    (options, arguement) = parser.parse_args()
    if  not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    if  not options.new_mac:
        parser.error("[-] Please specify a new mac address, use --help for more info")
    return options

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Changing the MAC address for "+interface+ "to" + new_mac)

options = get_args()
change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

mac_add_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

if mac_add_search_result:
    print(mac_add_search_result.group[0])
else:
    print("[-] Could not read the MAC address")