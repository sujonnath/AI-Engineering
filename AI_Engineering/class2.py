# Import Package, Get data from websit and display
#! pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import csv
import json

# Step 1: Fetch the webpage
url = "https://www.python.org"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
#print(soup)
# Step 2: Find the news section
news = soup.find("div",class_="medium-widget event-widget last")
headlines = news.find_all("li")
print("Latest Python News:")
for item in headlines:
  title= item.find("a").text.strip()
  date = item.find("time").text.strip()
  print(f"{date}-{title}")
# Step 3: Extract quotes and authors
url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
quotes_data = []

quotes = soup.find_all("div",class_="quote")
for quote in quotes:
  text = quote.find("span",class_="text").text.strip()
  author = quote.find("small",class_="author").text.strip()
  quotes_data.append({"quote": text,"author": author})
# Step 4: Save to Json
#with open("quotes.json","w",ending="utf-g") as json_file:
with open("quotes.json","w") as json_file2:
  json.dump(quotes_data,json_file2,indent=4)
  #json.dump(quotes_data,json_file, indent=4 , ensure_ascii=false)
  print("Saved to quotes.json")