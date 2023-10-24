import os
import sys
import gradio as gr

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(project_root)

from src.data_processing.news_parser import get_latest_news
from src.data_processing.translator import translate_text
from src.neural_network.bart_model import summarize_text

def summarize_and_translate():
    # Парсим последние новости
    latest_news = get_latest_news()

    if not latest_news:
        return "Failed to retrieve news."

    # Объединяем тексты новостей в один длинный текст
    news_text = [news["Article Content"] for news in latest_news][0][:250]
    print(1)

    # Суммаризируем текст
    summarized_text = summarize_text(news_text)
    print(2)

    # Переводим суммаризацию
    translated_text = translate_text(summarized_text)
    print(3)


    # в идеале сдампить json в строку и вернуть его для большей гибкости
    return f"""{latest_news[0].get('Title')}\n\n{translated_text}\n
Источник: {latest_news[0].get('Link')}\nGENERATED BY GLOBALVERSE@CARBONGROUP"""


with gr.Blocks() as blocks:
    with gr.Column():
        summarize_btn = gr.Button("Summarize and Translate")
        output_area = gr.Text(
            label="Your summarized news in Russian",
            placeholder="Nothing here :("
        )

    summarize_btn.click(
        summarize_and_translate,
        # TODO здесь может быть ваша ссылка
        # будет warning, что пропущен аргумент input
        outputs=[output_area]
    )
    blocks.launch()
