import requests
from bs4 import BeautifulSoup
import json
import logging

# Логирование
logging.basicConfig(filename='news_parser.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Конфигурация
URL = 'https://futurism.com/latest'

# Функция для удаления секции "More on Twitter" и "Share This Article"
def remove_unwanted_sections(soup):
    for unwanted_section in soup.find_all('p'):
        if "More on" in unwanted_section.get_text():
            unwanted_section.extract()

    tracking_section = soup.find('div', class_='tracking-[.05em] text-center uppercase font-hn text-futurism text-2 py-4')
    if tracking_section:
        tracking_section.extract()

# Функция для парсинга новости
def parse_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        remove_unwanted_sections(soup)
        title = soup.find('h1', class_='text-5xl').text
        article_content = soup.find('main', class_='post-content')
        paragraphs = article_content.find_all('p')
        article_text = '\n'.join([p.text for p in paragraphs])
        news_data = {
            "Title": title,
            "Article Content": article_text,
            "Link": url,
        }
        return news_data
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve the webpage: {e}")
        return None

# Функция для получения последних новостей
def get_latest_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.find_all('a', class_='block')[:5]

        news_list = [parse_news('https://futurism.com' + news.get('href')) for news in news_items]
        return [news_data for news_data in news_list if news_data]
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve the webpage: {e}")
        return None

if __name__ == '__main':
    latest_news = get_latest_news(URL)
    if latest_news:
        with open('news_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(latest_news, json_file, ensure_ascii=False, indent=4)
    else:
        logging.error("Не удалось получить доступ к сайту.")
