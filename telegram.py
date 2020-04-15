import telebot
import pyowm
from telebot import types

owm = pyowm.OWM("905c95dc8f833e9035b8f633fc478ee6", language = "ru")

bot = telebot.TeleBot("1147580820:AAHaQFebkCXVYcgzJsaBsch_kt8YD0sZx_Q")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Вот, что я умею: \n ---Пиши 'погода '")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if "погода" == (message.text).lower():
        bot.send_message(message.from_user.id, "Какой населенный пункт тебе нужен?")
        bot.register_next_step_handler(message, get_weather)
    else:
        bot.send_message(message.from_user.id, "Я отвечаю только на вопросы о погоде)")
        
@bot.message_handler(content_types=['text'])
def get_weather(message):
    place = (message.text).lower()
    try:
        observation = owm.weather_at_place(place)

        w = observation.get_weather()

        temp = w.get_temperature('celsius')["temp"]

        bot.send_message(message.from_user.id, "Сейчас на улице: " + w.get_detailed_status() + " " + str(round(temp)) + "°C")
        bot.send_message(message.from_user.id, "Скорость ветра: " + str(w.get_wind()["speed"]) + " м/с")
        bot.send_message(message.from_user.id, "Влажность воздуха: " + str(w.get_humidity()) + "%")
            
        bot.send_message(message.from_user.id, "Обращайся, если хочешь узнать погоду)")

    except:

        bot.send_message(message.from_user.id, "Прости, но я не нашел информацию по населенному пунктку '" + place + "'")
            
        
bot.polling(none_stop=True, interval=0)

