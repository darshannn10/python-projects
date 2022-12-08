#Scraping the website to find cheapeast graphics cards on the website

from encodings import search_function
from bs4 import BeautifulSoup
import requests
import re

search_term = input("What product do you want to search for : ")
#print("Initiating search for "+search_term)
url = f"https://www.newegg.ca/p/pl?d={search_term}&n=4131"

page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong

pages = int(str(page_text).split("/")[1].split(">")[-1][0])
#print(pages)

items_found = {}

for page in range(1, pages+1):
    url = f"https://www.newegg.ca/p/pl?d={search_term}&n=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    item = div.find_all(text=re.compile(search_term))
    for item in item:
        parent = item.parent
        link = None
        if parent.name != "a":
            continue
        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        price = next_parent.find(class_="price-current").strong.string
        
        items_found = print(item+" => price: "+(price.replace(",", "")))
        print("link : "+link)
        print()  

        # items_found[item] = {"price": int(price.replace(",", "")), "link": link}
        # print(items_found)

