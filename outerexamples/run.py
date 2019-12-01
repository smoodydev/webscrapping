import requests
from bs4 import BeautifulSoup

htmlPage = requests.get("https://www.google.com").text

soup = BeautifulSoup(htmlPage, "lxml")

print(soup.title.text)
