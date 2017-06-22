import urllib2
from bs4 import BeautifulSoup
q="http://www.mygola.com/ernakulam-d1004902/parking"
page=urllib2.urlopen(q)
soup=BeautifulSoup(page,'html.parser')
# name_box=soup.find_all(attrs={'class':'place-name'})
# name=name_box.text.strip()
# print name
# Run a loop to find all elements with specified class
# span, div, a, table or anything - HTML Tag
# place-name is a "class name" - attribute
for data in soup.find_all('span',attrs={"class" : "place-name"}):
    print data.text
