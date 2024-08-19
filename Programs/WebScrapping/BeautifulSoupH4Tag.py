import requests
from bs4 import BeautifulSoup


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
for tag in h4tags:
    print(tag.findNext('h4').findNext('a').get('title'))
    #print("product name " ,title)
    print("price ", tag.text)
    # iterate all tags