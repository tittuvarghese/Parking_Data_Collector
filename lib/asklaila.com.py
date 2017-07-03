# scrapped from asklaila.com
#Developed By-Saranya S kumar
# Date - 03-07-2017
# import all the libraries that we are going to use.
import urllib2
from bs4 import BeautifulSoup
# specify the url
req = urllib2.Request("https://www.asklaila.com/search/Ernakulam-Cochin/-/kalyana-mandapam/", headers={'User-Agent' : "Magic Browser"})
page = urllib2.urlopen( req )
# parse the html using beautiful soap and store in variable `soup`
soup=BeautifulSoup(page,'html.parser')
#find name
name=[]
for n in soup.find_all('h2',attrs={"class" : "resultTitle"}):
    name.append(n.text)

print name
#find subtitle
sub=[]
for r in soup.find_all('span',attrs={"class" : "resultSubTitle"}):
    sub.append(r.text)

print sub
#find address
address=[]
for p in soup.find_all('div',attrs={"class" : "col-xs-12 col-sm-12 col-md-12 col-lg-12 cardElement"}):
     address.append(p.text)

print address
#find specification
spec=[]
for s in soup.find_all('div',attrs={"class":"col-xs-12 col-sm-12 col-md-12 col-lg-12 cardElement bottomSpaceMargin"}):
    spec.append(s.text)

print spec


result=[]
result=zip(name,sub,address,spec)
#print data
print result
import csv
from datetime import datetime
# Opening CSV file / create
with open('wedding_halls_in_kochi_list.csv','wb')as csv_file:
    # Write Buffer
	writer=csv.writer(csv_file)
    # Writing Variables to csv file
	for row in result:
		writer.writerow(row)
