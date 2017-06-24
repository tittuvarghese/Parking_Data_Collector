import urllib2
from bs4 import BeautifulSoup
q="http://www.mygola.com/ernakulam-d1004902/parking"
page=urllib2.urlopen(q)
soup=BeautifulSoup(page,'html.parser')
name=[]
for n in soup.find_all('span',attrs={"class" : "place-name"}):
	name.append(n.text)
print name
address=[]
for a in soup.find_all(attrs={"style":"font-size:12px;padding-left:40px;"}):
	address.append(a.text)
print address
address=map(lambda each:each.replace('\t',''),address)
print address
address=map(lambda each:each.replace('\n',''),address)
print address
p=[]
p=zip(name,address)
print p
import csv
from datetime import datetime
with open('parking_lots_kochi.csv','wb')as file:
	writer=csv.writer(file)
	for row in p:
		writer.writerow(row)
