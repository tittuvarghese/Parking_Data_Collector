import urllib2
from bs4 import BeautifulSoup
c="https://area-codes.cybo.com/india/484_ernakulam/parking-lots-and-garages/?"
page=urllib2.urlopen(c)
soup=BeautifulSoup(page,'html.parser')
name=[]
for n in soup.find_all(attrs={"class":"e-bname ellipsis"}):
    name.append(n.text)

print name
rating=[]
for r in soup.find_all('span',attrs={"itemprop":"ratingValue"}):
    rating.append(r.text)

print rating
rating=map(lambda each:each.replace(u'\xa0',u''),rating)
print rating
phone_no=[]
for p in soup.find_all('span',attrs={"itemprop":"telephone"}):
     phone_no.append(p.text)

print phone_no
website=[]
for w in soup.find_all(attrs={"class":"web-link"}):
    website.append(w.text)

print website
address=[]
for a in soup.find_all('span',attrs={"class":"e-add ellipsis"}):
    address.append(a.text)

print address
des=[]
for d in soup.find_all('span',attrs={"class":"e-cat ellipsis"}):
    des.append(d.text)

print des

l="https://area-codes.cybo.com/india/484_ernakulam/parking-lots-and-garages/?p=2"
page=urllib2.urlopen(l)
soup=BeautifulSoup(page,'html.parser')
for n in soup.find_all(attrs={"class":"e-bname ellipsis"}):
    name.append(n.text)

print name
for r in soup.find_all('span',attrs={"itemprop":"ratingValue"}):
    rating.append(r.text)

print rating
rating=map(lambda each:each.replace(u'\xa0',u''),rating)
print rating
for p in soup.find_all('span',attrs={"itemprop":"telephone"}):
     phone_no.append(p.text)

print phone_no
for w in soup.find_all(attrs={"class":"web-link"}):
    website.append(w.text)

print website
for a in soup.find_all('span',attrs={"class":"e-add ellipsis"}):
    address.append(a.text)

print address
for d in soup.find_all('span',attrs={"class":"e-cat ellipsis"}):
    des.append(d.text)

print des
des=map(lambda each:each.replace(u'\xa0',u''),des)

par=[]
par=zip(name,rating,address,phone_no,website,des)
print par
import csv
from datetime import datetime
with open('parking_lots_kochi2.csv','wb')as file:
	writer=csv.writer(file)
	for row in par:
		writer.writerow(row)
