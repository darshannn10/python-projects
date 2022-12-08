from cgitb import strong
from bs4 import BeautifulSoup
import requests
import re

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.find_all("input", type="text")
for tag in tag:
    tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
    file.write(str(doc))