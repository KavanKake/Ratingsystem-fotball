import requests
from bs4 import BeautifulSoup

url = 'https://www.fotmob.com/nb/matches/barcelona-vs-young-boys/2xildd#4621538'
response = requests.get(url)

# If the page is accessible
if response.status_code == 200:
    page_content = response.text



soup = BeautifulSoup(page_content, 'html.parser')

# Now you can search for script tags or specific elements
scripts = soup.find_all('script')


import re

# Search for something that looks like an API URL
api_endpoints = re.findall(r'https?://[^\s"\']+', page_content)

# This would give you a list of all URLs, including potential API calls
print(api_endpoints)


