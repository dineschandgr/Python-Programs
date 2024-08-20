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
class_list = set()

h4_tag = soup.find('h4').text

limited_tags = soup.find_all('h4')

for tag in limited_tags:
    pass
    #print(tag)

#h4tags =  soup.find("h4", class_="price")
h4tags = soup.select('.price')
data = []
for tag in h4tags:
    try:
        #print("product name ",tag.findNext('h4').findNext('a').get('title'))
        #print("price ", tag.text)
        product_price = []
        product_price[0] = tag.findNext('h4').findNext('a').get('title')
        product_price[1] = tag.text
        data.append(product_price)

    except:
        print()
    # iterate all tags
print("data ",data)

# myfile = Path('scrapping-output.csv')
# with open(myfile, 'w') as csv_file_output:
#     writer = csv.writer(csv_file_output)
#     count = 0
#     for row in data:
#          if count == 0:
#              header = []
#              header[0] = "Product Name"
#              header[1] = "Price"
#              writer.writerow(header)
#          else:
#              writer.writerow(row)
# print("Script Completed")



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
