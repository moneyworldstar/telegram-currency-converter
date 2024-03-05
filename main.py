from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
import requests

app = Client("my_bot", api_id='хуй', api_hash='соси', bot_token='губой:тряси')

def calculate(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Я долбаёб: {str(e)}"

def convert_currency(amount, from_currency, to_currency):
    try:
        response = requests.get(f"https://v6.exchangerate-api.com/v6/ВАНЯ_ГЕЙ_КАРИНА_БЕГИ_ОТ_НЕГО/pair/{from_currency}/{to_currency}/{amount}")
        data = response.json()
        if data['result'] == 'success':
            return str(round(data['conversion_result'], 2))
        else:
            return f"Я долбаёб: {data['error-type']}"
    except Exception as e:
        return f"Я долбаёб: {str(e)}"

@app.on_inline_query()
def answer(client, inline_query):
    query = inline_query.query
    if not query:
        return

    result = "'calc:' для калькулятора, 'convert:' для конверта "
    title = "Что ты высрал?"
    description = "Пиши по нормальному"

    if query.startswith('calc:'):
        expression = query.replace('calc:', '')
        result = calculate(expression)
        title = f"{expression} = {result}"
        description = "тыч сюда чтоб высрать в чат"
        
    elif query.startswith('convert:'):
        parts = query.replace('convert:', '').split()
        if len(parts) == 4 and parts[2].lower() == 'to':
            amount, from_currency, to_currency = float(parts[0]), parts[1].upper(), parts[3].upper()
            result = convert_currency(amount, from_currency, to_currency)
            title = f"Conversion: {amount} {from_currency} = {result} {to_currency}"
            description = "тыч сюда чтоб высрать в чат"
        else:
            title = "Хуйня. Надо 'convert: *сумма* *валюта1* to *валюта2*'"
            description = "пиши по нормальному"

    inline_result = InlineQueryResultArticle(
        title=title,
        input_message_content=InputTextMessageContent(message_text=result),
        description=description,
        thumb_url="https://i.imgur.com/ed5XiTJ.png",  # Replace with your own thumbnail URL
        thumb_width=40,
        thumb_height=40
    )

    # Answer the inline query
    inline_query.answer(
        results=[inline_result],
        cache_time=1
    )

# Run the bot
app.run()