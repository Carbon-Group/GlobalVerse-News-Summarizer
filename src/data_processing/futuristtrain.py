import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def get_news_text(url_links, url_article):
    response_links = requests.get(url_links)

    if response_links.status_code == 200:
        soup_links = BeautifulSoup(response_links.text, 'html.parser')

        links = soup_links.find_all('a')

        news_texts = []

        for i in range(1, min(6, len(links))):
            link = links[i]
            href = link.get('href')

            parsed_url = urlparse(url_links)
            domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
            full_url = urljoin(domain, href)

            response_article = requests.get(full_url)

            if response_article.status_code == 200:
                soup_article = BeautifulSoup(response_article.text, 'html.parser')
                

                title = soup_article.find('title').get_text()
                
                text = ""
                paragraphs = soup_article.find_all('p')
                for paragraph in paragraphs:
                    text += paragraph.get_text() + '\n'
                
                news_texts.append((title, text))
            else:
                print(f"Не удалось получить доступ к ссылке {i}. Код ответа:", response_article.status_code)

        return news_texts
    else:
        print("Не удалось получить доступ к странице с ссылками. Код ответа:", response_links.status_code)

url_links = 'https://futurism.com/latest'

url_article = 'https://futurism.com/elon-musk-trouble-israel-palestine-violence'

news_texts = get_news_text(url_links, url_article)
for i, (title, text) in enumerate(news_texts, 1):
    print(f"Новость {i} - Заголовок: {title}")
    print("Текст:", text)
    print("\n")

