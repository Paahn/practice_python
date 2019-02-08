# Use the BeautifulSoup and requests
# Python packages to print out a list of
# all the article titles on the New York Times homepage.
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
soup = BeautifulSoup((requests.get(url)).text, features="lxml")

for line in soup.find_all(class_="css-d59ole esl82me2"):
    if line.a:
        print(line.a.text.replace("\n", " ").strip())
    else:
        print(line.contents[0].strip())=


