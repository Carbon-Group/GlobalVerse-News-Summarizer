import requests
from bs4 import BeautifulSoup
import json

# Функция для парсинга новости
def parse_news(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Не удалось получить доступ к странице: {url}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Функция для удаления секции "More on Twitter" и "Share This Article"
    for unwanted_section in soup.find_all('p'):
        if "More on" in unwanted_section.get_text():
            unwanted_section.extract()

    tracking_section = soup.find('div', class_='tracking-[.05em] text-center uppercase font-hn text-futurism text-2 py-4')
    if tracking_section:
        tracking_section.extract()

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

# Функция для получения последних 5 новостей
def get_latest_news():
    url = 'https://futurism.com/latest'
    response = requests.get(url)
    if response.status_code != 200:
        print("Не удалось получить доступ к сайту.")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.find_all('a', class_='block')[:5]

    news_list = [parse_news('https://futurism.com' + news.get('href')) for news in news_items]
    return [news_data for news_data in news_list if news_data]

if __name__ == '__main__':
    latest_news = get_latest_news()
    if latest_news:
        with open('news_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(latest_news, json_file, ensure_ascii=False, indent=4)
    else:
        print("Не удалось получить доступ к сайту.")
