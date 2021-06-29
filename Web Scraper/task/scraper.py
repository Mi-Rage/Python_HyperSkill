import requests
import string
from bs4 import BeautifulSoup

url_path = "https://www.nature.com/nature/articles"
response = requests.get(url_path)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('article')
for article in articles:
    category = article.find('span', {'class': 'c-meta__type'}).text
    if category.lower() == 'news':
        print("----------------------")
        print(category)

        name = article.find('a').text
        for n in name:
            if n in string.punctuation:
                name = name.replace(n, '')
        name = name.replace(' ', '_')
        print(name)

        href = 'https://www.nature.com' + article.find('a', {'class': 'c-card__link u-link-inherit'}).get('href')
        print(href)

        article_response = requests.get(href)
        article_soup = BeautifulSoup(article_response.content, 'html.parser')
        article_div = article_soup.find('div', {'class': 'c-article-body u-clearfix'}).text
        article_text = article_div.replace('\n', '')
        print(article_text)

        with open(name + ".txt", 'wb') as file:
            file.write(article_text.encode())
