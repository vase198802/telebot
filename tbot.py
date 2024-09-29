import requests
from telebot import types
import telebot
from bs4 import BeautifulSoup as b

URL1 = 'https://horo.mail.ru/prediction/aries/today/'
API_KEY = '5737874370:AAEACwtnBOUwa2UzkEX4Q6Gnnz8cDddZ6ic'
def parser_aries(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope_aries = soup.find_all('div', class_='article__text')
    return [c.text for c in horoscope_aries]

list_aries = parser_aries(URL1)
#Телец
URL2 = 'https://horo.mail.ru/prediction/taurus/today/'
def parser_taurus(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope_taurus = soup.find_all('div', class_='article__text')
    return [c.text for c in horoscope_taurus]
list_taurus = parser_taurus(URL2)
#Близнецы
URL3 = 'https://horo.mail.ru/prediction/gemini/today/'
def parser_twins(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope_twins = soup.find_all('div', class_='article__text')
    return [c.text for c in horoscope_twins]
list_twins = parser_twins(URL3)
#Рак
URL4 = 'https://horo.mail.ru/prediction/cancer/today/'
def parser_crayfish(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope_crayfish = soup.find_all('div', class_='article__text')
    return [c.text for c in horoscope_crayfish]
list_crayfish = parser_crayfish(URL4)
#Лев
URL5 = 'https://horo.mail.ru/prediction/leo/today/'
def parser_lion(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope_lion = soup.find_all('div', class_='article__text')
    return [c.text for c in horoscope_lion]
list_lion = parser_lion(URL5)
#Дева
URL6 = 'https://horo.mail.ru/prediction/virgo/today/'
def parser_virgo(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope_virgo = soup.find_all('div', class_='article__text')
    return [c.text for c in horoscope_virgo]
list_virgo = parser_virgo(URL6)
#Весы
URL7 = 'https://horo.mail.ru/prediction/libra/today/'
def parser_scales(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope_scales = soup.find_all('div', class_='article__text')
    return [c.text for c in horoscope_scales]
list_scales = parser_scales(URL7)
#Скорпион
URL8 = 'https://horo.mail.ru/prediction/scorpio/today/'
def parser_scorpion(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope_scorpion = soup.find_all('div', class_='article__text')
    return [c.text for c in horoscope_scorpion]
list_scorpion = parser_scorpion(URL8)
#Стрелец
URL9 = 'https://horo.mail.ru/prediction/sagittarius/today/'
def parser_sagittarius(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope_sagittarius = soup.find_all('div', class_='article__text')
    return [c.text for c in horoscope_sagittarius]
list_sagittarius = parser_sagittarius(URL9)
#Козерог
URL10 = 'https://horo.mail.ru/prediction/capricorn/today/'
def parser_capricorn(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope_capricorn = soup.find_all('div', class_='article__text')
    return [c.text for c in horoscope_capricorn]
list_capricorn = parser_capricorn(URL10)
#Водолей
URL11 = 'https://horo.mail.ru/prediction/aquarius/today/'
def parser_aquarius(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope_aquarius = soup.find_all('div', class_='article__text')
    return [c.text for c in horoscope_aquarius]
list_aquarius = parser_aquarius(URL11)
#Рыбы
URL12 = 'https://horo.mail.ru/prediction/pisces/today/'
def parser_fish(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope_fish = soup.find_all('div', class_='article__text')
    return [c.text for c in horoscope_fish]
list_fish = parser_fish(URL12)

bot = telebot.TeleBot('8039836946:AAHyyI4156WFz1Oe97H5chQnAB6it43GEso')
@bot.message_handler(['начать'])
def hello(message):
    button = types.InlineKeyboardMarkup(row_width=4)
    cnopka = types.InlineKeyboardButton('Овен', callback_data='1')
    cnopka2 = types.InlineKeyboardButton('Телец', callback_data='2')
    cnopka3 = types.InlineKeyboardButton('Близнецы', callback_data='3')
    cnopka4 = types.InlineKeyboardButton('Рак', callback_data='4')
    cnopka5 = types.InlineKeyboardButton('Лев', callback_data='5')
    cnopka6 = types.InlineKeyboardButton('Дева', callback_data='6')
    cnopka7 = types.InlineKeyboardButton('Весы', callback_data='7')
    cnopka8 = types.InlineKeyboardButton('Скорпион', callback_data='8')
    cnopka9 = types.InlineKeyboardButton('Стрелец', callback_data='9')
    cnopka10 = types.InlineKeyboardButton('Козерог', callback_data='10')
    cnopka11 = types.InlineKeyboardButton('Водолей', callback_data='11')
    cnopka12 = types.InlineKeyboardButton('Рыбы', callback_data='12')
    button.add(cnopka, cnopka2, cnopka3, cnopka4, cnopka5, cnopka6, cnopka7, cnopka8, cnopka9, cnopka10, cnopka11, cnopka12)
    bot.send_message(message.chat.id, 'Привет! Гороскоп на сегодня выбери свой знак задиака:', reply_markup=button)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == '1':
            bot.send_message(call.message.chat.id, list_aries[0])
        elif call.data == '2':
            bot.send_message(call.message.chat.id, list_taurus[0])
        elif call.data == '3':
            bot.send_message(call.message.chat.id, list_twins[0])
        elif call.data == '4':
            bot.send_message(call.message.chat.id, list_crayfish[0])
        elif call.data == '5':
            bot.send_message(call.message.chat.id, list_lion[0])
        elif call.data == '6':
            bot.send_message(call.message.chat.id, list_virgo[0])
        elif call.data == '7':
            bot.send_message(call.message.chat.id, list_scales[0])
        elif call.data == '8':
            bot.send_message(call.message.chat.id, list_scorpion[0])
        elif call.data == '9':
            bot.send_message(call.message.chat.id, list_sagittarius[0])
        elif call.data == '10':
            bot.send_message(call.message.chat.id, list_capricorn[0])
        elif call.data == '11':
            bot.send_message(call.message.chat.id, list_aquarius[0])
        elif call.data == '12':
            bot.send_message(call.message.chat.id, list_fish[0])


bot.polling()