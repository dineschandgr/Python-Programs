import requests
from bs4 import BeautifulSoup
import csv
from pathlib import Path

# Making a GET request
r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')

# check status code for response received
# success code - 200
#print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
#h4tags =  soup.find("h4", class_="price")
h4tags = soup.select('.price')
data = []
for tag in h4tags:
    try:
        #print("product name ",tag.findNext('h4').findNext('a').get('title'))
        #print("price ", tag.text)
        product_price = []
        product_price.append(tag.findNext('h4').findNext('a').get('title'))
        product_price.append(tag.text)
        data.append(product_price)

    except Exception as e:
        print("error ",e)
    # iterate all tags
print("data ",data)

myfile = Path('scrapping-output.csv')
with open(myfile, 'w') as csv_file_output:
    writer = csv.writer(csv_file_output)
    count = 0
    for row in data:
         if count == 0:
             header = []
             header.append("Product Name")
             header.append("Price")
             writer.writerow(header)
         else:
             writer.writerow(row)
         count += 1
print("Script Completed")



#r = requests.get('https://www.flipkart.com/laptops-store?otracker=nmenu_sub_Electronics_0_Laptops')

# check status code for response received
# success code - 200
#print(r)

# Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# limited_tags = soup.find_all('td')
# for tag in limited_tags:
#     #print("tag ",tag)
#     print(tag.findNext('span').findNext('a').get('title'))
# # Parse td's styles
# for tag in soup.findAll(attrs={'style':'font-family:Lucida Sans Unicode'}):
#     print("tag ",tag)
