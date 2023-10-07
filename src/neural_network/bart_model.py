import torch
from transformers import BartTokenizer, BartForConditionalGeneration

# Проверка доступности GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Загрузка модели BART для суммаризации на GPU
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)
model.to(device)


def summarize_text(input_text, max_input_length=1024, max_summary_length=None):
    # Замена символа новой строки на пробел
    input_text = input_text.replace('\n', ' ')
    
    # Токенизация текста
    inputs = tokenizer(input_text, return_tensors='pt', max_length=max_input_length, truncation=True).to(device)

    # Генерация суммаризации
    if max_summary_length is None:
        max_summary_length = len(input_text) // 2

    summary_ids = model.generate(
        inputs['input_ids'],
        max_length=max_summary_length,
        min_length=max_summary_length // 2,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )

    # Декодирование и возврат суммаризации
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Пример использования:
input_text = """All-in-one desktop computers are a great space-saving solution for folks who work at home or in a cramped office. But what if you want to work from a coffee shop? Laptop's just don't offer a big-screen experience, so HP has made the AIO mobile with the Envy Move.

Though I work from home, I use a laptop rather than a desktop PC – but I have it cabled to a computer monitor over HDMI because the bigger screen makes for more comfortable viewing.

HP has combined the portable convenience of a laptop with power of an all-in-one PC by building in an 83-Wh Li-ion battery for up to four hours away from the wall outlet. The AIO supports fast-charging for a top-up to 50% capacity in around 45 minutes. There's a built-in carry handle, two swivel kickstand feet, and it even sports a pocket at the back to carry the included Bluetooth keyboard (a mouse is an optional extra)."""
summarized_text = summarize_text(input_text)
print(summarized_text)
