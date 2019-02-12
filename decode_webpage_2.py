# Using the requests and BeautifulSoup Python libraries,
# print to the screen the full text of the article on
# this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# The article is long, so it is split up between 4 pages.
# Your task is to print out the text to the screen so that
# you can read the full article without having to click any buttons.
import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
soup = BeautifulSoup((requests.get(url)).text, "lxml")
for line in soup.find_all('section', class_="content-section"):
        print(line.text)