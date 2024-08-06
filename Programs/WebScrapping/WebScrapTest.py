import requests

# Making a GET request
r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)