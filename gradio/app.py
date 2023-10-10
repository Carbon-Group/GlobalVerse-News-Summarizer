import os
import sys
import gradio as gr

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(project_root)

from src.neural_network.bart_model import summarize_text

def dummy(text):
    return summarize_text(text)


with gr.Blocks() as blocks:
    with gr.Row():
        with gr.Column():
            input_field = gr.Text(
                label="Input text",
                placeholder="Your text here..."
            )
            summarize_btn = gr.Button("Summarize")

        with gr.Column():
            output_area = gr.Text(
                label="Your summarized new",
                placeholder="Nothing here :("
            )

    # renders text, also updates state of button
    summarize_btn.click(
        dummy,
        inputs=[input_field],
        outputs=[output_area]
    )
    # just updates state of buttons
    input_field.change(
        fn=lambda: ("Summarize", "Copy"),
        inputs=[],
        outputs=[summarize_btn],
    )

    blocks.launch()
