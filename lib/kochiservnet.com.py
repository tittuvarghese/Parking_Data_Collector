# scrapped from kochiservnet.com
#Developed By-Saranya S kumar
# Date - 27-06-2017
# import all the libraries that we are going to use.
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#specify the url
q="http://www.kochiservnet.com/services/services_action_view.php/General%20/Halls%20and%20Auditoriums"
# query the website and return the html to the variable ‘page’
page=urllib2.urlopen(q)
# parse the html using BeautifulSoup and store in a variable 'soup'
soup=BeautifulSoup(page,'html.parser')

# Find Listing Blocks
for result in soup.find_all('div',attrs={"class":"list"}):
    # Extract Listing Name
    listingName = result.findNext('div',attrs={"class" : "listTitle"})
    # Extract Listing Address
    listingAddress = result.findNext('div',attrs={"class" : "listContent"})
    # Printing the Data
    print listingName.text, " - " + listingAddress.text
    # Opening CSV file / create
    with open("kochi_halls_auditorium_list.csv", "a") as csv_file:
        # Write Buffer
        writer = csv.writer(csv_file)
        # Writing Variables to csv file
        writer.writerow([listingName.text, listingAddress.text, datetime.now()])
