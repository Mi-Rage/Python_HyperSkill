import requests
from bs4 import BeautifulSoup

url_path = input()
r = requests.get(url_path, headers={'Accept-Language': 'en-US,en;q=0.5'})
soup = BeautifulSoup(r.content, 'html.parser')
result = {}
try:
    title = soup.find('title')
    result['title'] = title.text
    summary = soup.find('div', class_='summary_text').get_text()
    result['description'] = summary.strip()
    print(result)
except (LookupError, AttributeError):
    print("Invalid movie page!")

