import requests
import socket
import json

domain = input("Enter domain: ")
req = requests.get("https://"+domain)
print(req.headers, "\n")

ip_addr = socket.gethostbyname(domain)
print(f"IP address of {domain} is {ip_addr}", "\n")

req2 = requests.get("https://ipinfo.io/" + ip_addr +"/json")
data = json.loads(req2.text)
print("Location of" + domain +" is "+ data["loc"], "\n")