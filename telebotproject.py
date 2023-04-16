import telebot
import re
import urllib.parse
import urllib.request
import bs4


def getReport(myurl):
    try:
        m = myurl[79]
        m = m[1:-3]
        reponse = urllib.request.Request(str(m))
        html = urllib.request.urlopen(reponse).read().decode("utf-8")
        soup = bs4.BeautifulSoup(html, 'html.parser')
        pattern = r'http://v.virscan.org/\w+'
        vLinks = soup.find_all('a', href=re.compile(pattern))
        if len(vLinks) == 0:
            return 'safe'
        else:
            for vlink in vLinks:
                url3 = urllib.parse.quote(vlink['href'])
                url3 = url3.replace('http%3A', 'http:')
                if vlink.has_attr('alt'):
                    return 'Unsafe'
                else:
                    return 'safe'
    except:
        return 'Unsafe'
def password():
    return "2108338382:AAG4942rp7u5HeAPD0rKYlNrqY2dQJDV5C4"
bot = telebot.TeleBot(password())

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я телеграм бот для проверки сайтов на наличие вирусов.\n' +
                     'Давай объясню, как я работаю:\n' +
                     '1) Ты вводишь ссылку на сайт\n' +
                     '2) Я проверяю эту ссылку с помощью своих баз данных\n' +
                     '3) Отвечаю тебе)\n' + 'Если у вас есть какой-то вопрос или проблема, то скажите "/помощь"(только не забудь про /), и я дам вам ссылку на чат с разработчиком,чтобы вы задачи свой вопрос'
                                            'Пока мы не начали проверять, предлагаю тебе посетить наш сайт. Там ты найдешь много интересной информации!!))')

@bot.message_handler(commands=['помощь'])
def help(message):
    bot.send_message(message.chat.id,
                     'Ссылка для связи с разработчиком: https://t.me/user_abraham , он ответит на твой вопрос в течение часа.'
                     )

@bot.message_handler(content_types=['text'])
def answer(message):
    if 'http' in str(message) or 'www' in str(message):
        m = list(str(message).split())
        if getReport(m) == 'safe':
            bot.send_message(message.chat.id, 'Все хорошо! Сайт безопасный')
        else:
            bot.send_message(message.chat.id, 'Похоже это не безопаный сайт')

    else:
        bot.send_message(message.chat.id, 'Похоже вы ввели что то не так) Попробуйте еще раз')


bot.polling()
