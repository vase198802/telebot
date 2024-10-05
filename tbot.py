import telebot
import requests
from bs4 import BeautifulSoup
import datetime



try:
    bot = telebot.TeleBot('8039836946:AAHyyI4156WFz1Oe97H5chQnAB6it43GEso')

    markup1 = telebot.types.InlineKeyboardMarkup()

    oven = telebot.types.InlineKeyboardButton(text='♈Овен♈',
                                              callback_data='oven')
    telec = telebot.types.InlineKeyboardButton(text='♉Телец♉',
                                               callback_data='telec')
    bliznec = telebot.types.InlineKeyboardButton(text='♊Близнец♊',
                                                 callback_data='bliznec')
    rak = telebot.types.InlineKeyboardButton(text='♋Рак♋',
                                             callback_data='rak')
    lev = telebot.types.InlineKeyboardButton(text='♌Лев♌',
                                             callback_data='lev')
    deva = telebot.types.InlineKeyboardButton(text='♍Дева♍',
                                              callback_data='deva')
    vesy = telebot.types.InlineKeyboardButton(text='♎Весы♎',
                                              callback_data='vesy')
    skorpion = telebot.types.InlineKeyboardButton(text='♏Скорпион♏',
                                                  callback_data='scorpion')
    strelec = telebot.types.InlineKeyboardButton(text='♐Стрелец♐',
                                                 callback_data='strelec')
    kozerog = telebot.types.InlineKeyboardButton(text='♑Козерог♑',
                                                 callback_data='kozerog')
    aqua = telebot.types.InlineKeyboardButton(text='♒Водолей♒',
                                              callback_data='aqua')
    fish = telebot.types.InlineKeyboardButton(text='♓Рыбы♓',
                                              callback_data='fish')

    markup1.add(oven, telec)
    markup1.add(bliznec, rak)
    markup1.add(lev, deva)
    markup1.add(vesy, skorpion)
    markup1.add(strelec, kozerog)
    markup1.add(aqua, fish)

    @bot.message_handler(commands=['start'])
    def start_msg(message):
        bot.send_message(message.chat.id,
                         text=f'Приветствую <b>{message.chat.first_name}</b>! Выберите ваш знак зодиака:',
                         reply_markup=markup1, parse_mode='html')

    @bot.message_handler(content_types=['text'])
    def send_msg(message):
        if message.text:
            bot.send_message(message.chat.id,
                             'Ссылка на бота: '
                             'https://t.me/horoscop198802bot')

    @bot.callback_query_handler(func=lambda call: True)
    def query_handler(call):
        if call.data == 'oven':
            res = requests.get(
                'https://horo.mail.ru/prediction/aries/today/').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
        elif call.data == 'telec':
            res = requests.get(
                'https://horo.mail.ru/prediction/taurus/today/').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
        elif call.data == 'bliznec':
            res = requests.get(
                'https://horo.mail.ru/prediction/gemini/today/').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
        elif call.data == 'rak':
            res = requests.get(
                'https://horo.mail.ru/prediction/cancer/today/').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
        elif call.data == 'lev':
            res = requests.get(
                'https://horo.mail.ru/prediction/leo/today/').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
        elif call.data == 'deva':
            res = requests.get(
                'https://horo.mail.ru/prediction/virgo/today/').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
        elif call.data == 'vesy':
            res = requests.get(
                'https://horo.mail.ru/prediction/libra/today/').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
        elif call.data == 'scorpion':
            res = requests.get(
                'https://horo.mail.ru/prediction/scorpio/today/').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
        elif call.data == 'strelec':
            res = requests.get(
                'https://horo.mail.ru/prediction/sagittarius/today/').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
        elif call.data == 'kozerog':
            res = requests.get(
                'https://horo.mail.ru/prediction/capricorn/today/').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
        elif call.data == 'aqua':
            res = requests.get(
                'https://horo.mail.ru/prediction/aquarius/today/').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
        elif call.data == 'fish':
            res = requests.get(
                'https://horo.mail.ru/prediction/pisces/today/').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
        else:
            pass


    bot.polling(none_stop=True, interval=0)

except Exception:
    pass