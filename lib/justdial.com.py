# scrapped from justdial.com
#Developed By-Saranya S kumar
# Date - 29-06-2017
# import all the libraries that we are going to use.
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
#specify the url
req = urllib2.Request("https://www.justdial.com/Kochi/Banquet-Halls/nct-10035861", headers={'User-Agent' : "Magic Browser"})
page = urllib2.urlopen( req )
# parse the html using BeautifulSoup and store in a variable 'soup'
soup=BeautifulSoup(page,'html.parser')

# Find Listing Blocks
for result in soup.find_all('div',attrs={"class":"store-details"}):
    # Extract Listing Name
    listingName = result.findNext('h4',attrs={"class" : "store-name"})
    # Extract Listing Address
    listingAddress = result.findNext('span',attrs={"class" : "mrehover"})
    #print listingAddress
    # Extract Listing Phone Number
    listingPhone = result.findNext('p',attrs={"class" : "contact-info "})
    # Printing the Data
    #print listingName
    print listingName.text, " - " + listingAddress.text, " - ", listingPhone.text
    # Opening CSV file / create
    with open("justdial.com_hotel.csv", "a") as csv_file:
        # Write Buffer
        writer = csv.writer(csv_file)
        # Writing Variables to csv file
        writer.writerow([listingName.text, listingAddress.text, listingPhone.text, datetime.now()])
