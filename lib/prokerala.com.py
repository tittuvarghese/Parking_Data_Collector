# scrapped from prokerala.com
#Developed By-Saranya S kumar
# Date - 29-06-2017
# import all the libraries that we are going to use.
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#specify the url
q="http://www.prokerala.com/hospitals/hospitals-in-ernakulam.html"
# query the website and return the html to the variable ‘page’
page=urllib2.urlopen(q)
# parse the html using BeautifulSoup and store in a variable 'soup'
soup=BeautifulSoup(page,'html.parser')

# Find Listing Blocks
for result in soup.find_all('div',attrs={"class":"list-details ellipsis"}):
    # Extract Listing Name
    listingName = result.findNext('span',attrs={"itemprop" : "name"})
    # Extract Listing Address
    listingAddress = result.findNext('div',attrs={"itemprop" : "address"})
    #print listingAddress
    # Printing the Data
    print listingName.text, " - " + listingAddress.text
    # Opening CSV file / create
    with open("hospitals_in_kochi_file.csv", "a") as csv_file:
        # Write Buffer
        writer = csv.writer(csv_file)
        # Writing Variables to csv file
        writer.writerow([listingName.text, listingAddress.text, datetime.now()])
