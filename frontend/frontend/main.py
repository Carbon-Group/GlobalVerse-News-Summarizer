import gradio as gr
import pyperclip


def dummy(name):
    return "Hello " + name, "Summarized!"


def copy_to_clipboard(text):
    pyperclip.copy(text)
    return "Copied!"


with gr.Blocks() as blocks:
    gr.Markdown(
        "# Hello from GlobalVerse!\n"
        "## This is demo interface. Stay patient, please..."
    )

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
            copy_button = gr.Button("Copy")

    # renders text, also updates state of button
    summarize_btn.click(
        dummy,
        inputs=[input_field],
        outputs=[output_area, summarize_btn]
    )
    # just updates state of buttons
    input_field.change(
        fn=lambda: ("Summarize", "Copy"),
        inputs=[],
        outputs=[summarize_btn, copy_button],
    )
    copy_button.click(
        copy_to_clipboard,
        inputs=[output_area],
        outputs=[copy_button],
    )

    blocks.launch()
