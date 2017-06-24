# Scrapped from mygola.com
# Developed By-Nimiya Joseph
# Date - 24-06-2017
# First, we need to import all the libraries that we are going to use.
import urllib2
from bs4 import BeautifulSoup
# specify the url
q="http://www.mygola.com/ernakulam-d1004902/parking"
# query the website and return the html to the variable ‘page’
page=urllib2.urlopen(q)
# parse the html using beautiful soap and store in variable `soup`
soup=BeautifulSoup(page,'html.parser')
name=[]
# Take out the <span> of name and get its values
for n in soup.find_all('span',attrs={"class" : "place-name"}):
	name.append(n.text)
print name
address=[]
for a in soup.find_all(attrs={"style":"font-size:12px;padding-left:40px;"}):
	address.append(a.text)
print address
#To remove '\t' and '\n'
address=map(lambda each:each.replace('\t',''),address)
print address
address=map(lambda each:each.replace('\n',''),address)
print address
# create another array p
p=[]
# store the details in row wise
p=zip(name,address)
print p
import csv
from datetime import datetime
# open a csv file with append, so old data will not be erased
with open('parking_lots_kochi.csv','a')as file:
	writer=csv.writer(file)
	for row in p:
		writer.writerow(row)
