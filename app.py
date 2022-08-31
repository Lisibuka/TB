import telebot
import json
import requests


TOKEN = '5570263703:AAHqzgXnwEKWhtiwkMOvfwxCFKUt9jY3aQU'

bot = telebot.TeleBot(TOKEN)


keys = {
    'евро': 'EUR',
    'доллар': 'USD',
    'рубль': 'RUB',
}



@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начат работу введите команду боту в следующем формате:\n<имя валюты, цену которой он хочет узнать> \
    <имя валюты, в которой надо узнать цену первой валюты> \
    <количество первой валюты>'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    base, sym, amount = message.text.split(' ')
    r = requests.get(f"https://api.exchangeratesapi.io/latest?base={base}&symbols={sym}")
    resp = json.loads(r.content)
    new_price = resp['rates'][sym] * float(amount)
    bot.reply_to(message, f"Цена {amount} {base} в {sym} : {new_price}")    

bot.polling() 
    










