import requests
from bs4 import BeautifulSoup

with open("example.html") as htmlPage:
    soup = BeautifulSoup(htmlPage, "lxml")



titlematch = soup.title.text

matchid = soup.find("div", id="titlesection")
matchclass = soup.find("div", class_="footer")



for i in soup.find_all("div", class_="articleblock"):
    print(i.h2.text)
    print(i.p.text)




print(matchid.text)
print(matchclass.text)




# ###############    SHOWS THE NICE VERSION
# print(soup.prettify())
    