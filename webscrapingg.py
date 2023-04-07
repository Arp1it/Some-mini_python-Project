# requirements - html5lib, requests, bs4

import requests
from bs4 import BeautifulSoup
url = "https://docs.python.org/3/"

# Get the HTML
r = requests.get(url)
htmlcontent = r.content
# print(htmlcontent)

# Parse the HTML
soup = BeautifulSoup(htmlcontent, "html.parser")
# print(soup)
# print(soup.prettify)

# HTML Tree Traversal

# Commonly used types of objects
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# 4. Comment

# get the title of the html page
title = soup.title
print(title)
print(title.string)

