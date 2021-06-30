import requests
import string
import os
from bs4 import BeautifulSoup

pages = int(input())
types_articles = input()

current_directory = os.getcwd()

for page in range(pages):
    directory_to_save = 'Page_' + str(page + 1)
    os.mkdir(directory_to_save)
    os.chdir(directory_to_save)

    url_path = "https://www.nature.com/nature/articles"
    parameter = {'searchType': 'journalSearch', 'sort': 'PubDate', 'page': page + 1}
    response = requests.get(url_path, params=parameter)
    print(response.url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article')

    for article in articles:
        category = article.find('span', {'class': 'c-meta__type'}).text
        if category == types_articles:
            print("----------------------")
            print(category)

            name = article.find('a').text
            for n in name:
                if n in string.punctuation:
                    name = name.replace(n, '')
            name = name.replace(' ', '_')
            print(name)

            href = 'https://www.nature.com' + article.find('a', {'class': 'c-card__link u-link-inherit'}).get(
                'href')
            print(href)

            article_response = requests.get(href)
            article_soup = BeautifulSoup(article_response.content, 'html.parser')
            article_div = ""
            try:
                article_div = article_soup.find('div', {'class': 'article-item__body'}).text
            except AttributeError:
                try:
                    article_div = article_soup.find('div', {'class': 'c-article-body u-clearfix'}).text
                except AttributeError:
                    print("WOW! Attribute error")

            article_text = article_div.replace('\n', '')
            print(article_text)

            with open(name + ".txt", 'wb') as file:
                file.write(article_text.encode())
    os.chdir(current_directory)
