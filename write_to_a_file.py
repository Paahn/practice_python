# Take the code from the How To Decode A Website exercise
# and instead of printing the results to a screen, write the results to a txt file.
# Ask the user to specify the name of the output file that will be saved.
from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
soup = BeautifulSoup((requests.get(url)).text, features="lxml")
file_title = input("Enter file name: ")

with open(file_title, 'w') as f:
    for line in soup.find_all(class_="css-d59ole esl82me2"):
        if line.a:
            f.write(line.a.text.replace("\n", " ").strip())
        else:
            f.write(line.contents[0].strip())

