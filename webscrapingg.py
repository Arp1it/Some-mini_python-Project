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
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p)
# print(soup2.p.string)
# print(type(soup2.p.string))


# get the title of the html page
title = soup.title
# print(title)
# print(title.string)

# Get all the paragraphs from the page
paras = soup.find_all("p")
# print(paras)

# Get all the anchor tags from the page
anchors = soup.find_all("a")
# print(anchors)

# Get all the links on the page
all_links = set()
for link in anchors:
    if link.get("href") != "#":
        all_links.add("https://docs.python.org/3/" + link.get("href"))

# for i in all_links:
#     print(i)


# Get First element in the HTML page
# print(soup.find("div"))

# Get classes of any element in the HTML page
# print(soup.find("div")["class"])

# find all the elements with class mobile-nav
# print(soup.find_all("div", class_="mobile-nav"))

# Get the text from the tags/soup
# print(soup.find("p").get_text())
# print(soup.get_text())


tagfindingid = soup.find(id="cpython-language-and-version")
# print(tagfindingid)
a = tagfindingid.children
# for i in a:
#     print(i)

# print(tagfindingid.contents)
c = tagfindingid.contents

# for elem in c:
#     print(elem)

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# Note - .childeren is faster than .contents

# for item in tagfindingid.strings:
#     print(item)
# for item in tagfindingid.stripped_strings:
#     print(item)

# print(tagfindingid.parent)
# print(tagfindingid.parents)

# for item in tagfindingid.parents:
#     print(item.name)

# print(tagfindingid.next_sibling)
# print(tagfindingid.previous_sibling)
# print(tagfindingid.next_sibling.next_sibling)
# print(tagfindingid.previous_sibling.previous_sibling)

# elem = soup.select('menuToggler')
# print(elem)
elem = soup.select('.mobile-nav')
print(elem)