#Functionality-scraping indiamart.com
#Developed by-Saranya S kumar
#Date-29-06-2017
#import all the libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
#specify the url
q="https://dir.indiamart.com/kochi/conference-hall.html"

page=urllib2.urlopen(q)
# parse the html using BeautifulSoup and store in a variable 'soup'
soup=BeautifulSoup(page,'html.parser')

# Find Listing Blocks
for result in soup.find_all('div',attrs={"class":"ldf"}):
    # Extract Listing Name
    listingName = result.findNext('a',attrs={"class" : "lcname"})
    # Extract Listing Address
    listingAddress = result.findNext('span',attrs={"class" : "clg"})
    #print listingAddress
    # Extract Listing Phone Number
    listingPhone = result.findNext('span',attrs={"class" : "ls_co phn"})
    # Printing the Data
    print listingName.text, " - " + listingAddress.text, " - ", listingPhone.text
    # Opening CSV file / create
    with open("busiest_spots_in_kochi_file.csv", "a") as csv_file:
        # Write Buffer
        writer = csv.writer(csv_file)
        # Writing Variables to csv file
        writer.writerow([listingName.text, listingAddress.text, listingPhone.text, datetime.now()])
