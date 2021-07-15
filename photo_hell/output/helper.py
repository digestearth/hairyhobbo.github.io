#!usr/bin/python3

import sys
from bs4 import BeautifulSoup
name = str(sys.argv[1]).replace("./", "")
filepath = str(sys.argv[2]).replace("./../", "")
filepath += name
htmldoc = str(sys.argv[3])

print(name, filepath, htmldoc)
with open(htmldoc) as inf:
    soup = BeautifulSoup(inf, 'html.parser')

#soup = BeautifulSoup(open(sys.argv[3]), 'html.parser')

head_tag = soup.new_tag("div", attrs={"class": "col-sm-6 col-md-4"})
middle_tag = soup.new_tag("a", attrs={"class":"lightbox", "href":filepath})
tail_tag = soup.new_tag("img", attrs={"alt": name, "src": filepath})

middle_tag.append(tail_tag)
head_tag.append(middle_tag)


soup.find("div", {"id": "gallery"}).append(head_tag)

for child in soup.find("div", {"id": "gallery"}).children:
    print(child)

with open(htmldoc, "w") as outf:
    outf.write(str(soup.prettify()))
