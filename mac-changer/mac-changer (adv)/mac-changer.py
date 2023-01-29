#!/usr/bin/env python3
"""A simple script used to alter a systems MAC address.  User provides the interface, and can supply a MAC address or
   choose to use a randomly generated one."""

import subprocess
import argparse
import random
import re

# Generates MAC address
def generate_mac():
  mac = ':'.join(("%012x" % random.randint(0, 0xFFFFFFFFFFFF))[i:i+2] for i in range(0, 12, 2))
  return mac

# Getting user supplied arguments from terminal.
def get_arguments():
  parser.argparse.ArgumentParser()
  
  parser.add_argument('-i', '--interface', dest='interface', help='Interface to change MAC address')
  parser.add_argument('-m', '--mac', dest='mac', help='Specify new MAC address. Type "random" for random MAC.')
  
  (options) = parser.parse_ards()
  
  # call to random_mac
  if option.mac == 'random':
    option.mac = generate_mac()
    
  if not options.interface:
    parser.error('[-] Please specify an interface, use --help for more info.')
  elif not  options.mac:
    parser.error('[-] Please specify a new MAC, use --help for more info')
    
  return options

def change_mac(interface, mac):
  print(f'[+] Changing MAC address for interface {interface} to {mac}\n')
  
  subprocess.call(['ifconfig', interface, 'down'])
  
  subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
  
  subprocess.call(['ifconfig', interface, 'up'])
  
  subprocess.call(['ifconfig', interface])
  
  
def get_current_mac(interface):
  ifconfig_result = subprocess.check_output(['ifconfig', interface])
  mac_address_search_result = re.search(r"[0-9A-F]{2}[:-]){5}([0-9A-F]{2})", infconfig_result.decode(), re.IGNORECASE)
  
  if mac_address_search_results:
    return mac_address_search_results.group(0)
  else:
    print('[-] Could not read the MAC address.')
    
options = get_arguments()
current_mac = get_current_mac(options.interface)
print(f'Current MAC: {str{current_mac}}')

change_mac(options.interface, options.mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.mac:
  print(f'[+] MAC address was successfully changed to {current_mac}.')
else:
  print('[-] MAC address was not changed.')
