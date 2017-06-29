# scrapped from infoisinfo.com
#Developed By-Saranya S kumar
# Date - 29-06-2017
# import all the libraries that we are going to use.
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
#specify the url
q="https://ernakulam-district.infoisinfo.co.in/search/supermarket"

page=urllib2.urlopen(q)
# parse the html using BeautifulSoup and store in a variable 'soup'
soup=BeautifulSoup(page,'html.parser')

# Find Listing Blocks
for result in soup.find_all('a',attrs={"class":"view-company"}):
    # Extract Listing Name
    listingName = result.findNext('span',attrs={"class" : "title-com"})
    # Extract Listing Address
    listingAddress = result.findNext('span',attrs={"class" : "streetAddress"})
    #print listingAddress
    # Printing the Data
    print listingName.text, " - " + listingAddress.text
    # Opening CSV file / create
    with open("infiisinfo_file.csv", "a") as csv_file:
        # Write Buffer
        writer = csv.writer(csv_file)
        # Writing Variables to csv file
        writer.writerow([listingName.text, listingAddress.text, datetime.now()])
