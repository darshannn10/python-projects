#!usr/bin/env python
import subprocess 
import time 
import optparse 
import re 

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", dest="interface", help="Choose interface.")
    parser.add_option("-m", dest="new_mac", help="Choose new MAC address.")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface, type --help for help")
    elif not options.new_mac:
        parser.error("Please specify a new MAC address, type --help for help")
    return options
    
def change_mac(interface, new_mac):
    print("[+] Change inferface " + interface + " to " + new_mac + " [+]")
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print("[+] Applying changes... [+]")
    time.sleep(1)

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_sr = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_sr:
        return (mac_sr.group(0))
    else:
        print("[-] Could not find MAC address [-]")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("[+] Current MAC = " + str(current_mac) + " [+]")
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("[+] MAC address successfully changed to " + current_mac + " [+]")
else:
    print("[+] ERROR! MAC address was not changed [+]")

#Example: python3 mac-changer.py -i eth0 -m 00:11:22:33:44:55