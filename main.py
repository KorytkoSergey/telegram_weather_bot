import requests
import os
from dotenv import load_dotenv
import telebot

load_dotenv()

key_for_bot = os.getenv('API_KEY_FROM_BOT')
key_for_weather = os.getenv('API_KEY_FROM_WEATHER')
bot = telebot.TeleBot(key_for_bot)

@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, "Введи название города")

@bot.message_handler(content_types='text')
def weather_info(message):
    city = message.text.strip().lower()
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key_for_weather}')
    req_data = data.json()
    temp = round(req_data["main"]['temp'] - 273.15)
    if req_data["weather"][0]["main"] == 'Rain':
        weather = 'Дождь🌧'
    elif req_data["weather"][0]["main"] == 'Clear':
        weather = 'Ясно🌞'
    elif req_data["weather"][0]["main"] == 'Clouds':
        weather = 'Облачно☁️'
    else:
        weather = req_data["weather"][0]["main"]
    bot.reply_to(message, f'температура {temp} градусов С\n {weather}')

bot.polling()


