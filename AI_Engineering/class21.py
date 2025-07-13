import requests
from bs4 import BeautifulSoup
import csv
import json


url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
quotes_data = []
print(soup)
quotes = soup.find_all("div",class_="quote")
#print(quotes)
for quote in quotes:
  text = quote.find("span",class_="text").text.strip()
  author = quote.find("small",class_="author").text.strip()
  quotes_data.append({"quote": text,"author": author})
  print(text)
# Step 4: Save to Json
#with open("quotes.json","w",ending="utf-g") as json_file:
with open("quotes.json","w") as json_file2:
  json.dump(quotes_data,json_file2,indent=4)
  #json.dump(quotes_data,json_file, indent=4 , ensure_ascii=false)
  print("Saved to quotes.json")