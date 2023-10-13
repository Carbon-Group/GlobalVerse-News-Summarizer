import os
import sys
import gradio as gr

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(project_root)

from src.data_processing.news_parser import get_latest_news
from src.neural_network.bart_model import summarize_text
from src.data_processing.translator import translate_text

def summarize_and_translate(text):
    # Парсим последние новости
    latest_news = get_latest_news()

    if not latest_news:
        return "Failed to retrieve news."

    # Объединяем тексты новостей в один длинный текст
    news_text = [news["Article Content"] for news in latest_news][0][:50]
    print("1")

    # Суммаризируем текст
    summarized_text = summarize_text(news_text)
    print("2")

    # Переводим суммаризацию
    translated_text = translate_text(summarized_text)
    print("3")

    return translated_text

with gr.Blocks() as blocks:
    with gr.Row():
        with gr.Column():
            input_field = gr.Text(
                label="Input text",
                placeholder="Your text here..."
            )
            summarize_btn = gr.Button("Summarize and Translate")

        with gr.Column():
            output_area = gr.Text(
                label="Your summarized news in Russian",
                placeholder="Nothing here :("
            )

    # renders text, also updates state of button
    summarize_btn.click(
        summarize_and_translate,
        inputs=[input_field],
        outputs=[output_area]
    )
    # just updates state of buttons
    input_field.change(
        fn=lambda: ("Summarize and Translate", "Copy"),
        inputs=[],
        outputs=[summarize_btn],
    )

    blocks.launch()
