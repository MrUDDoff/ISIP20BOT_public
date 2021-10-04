import telebot;
from telebot import types
import requests
from bs4 import BeautifulSoup
import datetime
from datetime import datetime

bot = telebot.TeleBot('TOKEN');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/zr":
        keyboard = types.InlineKeyboardMarkup()
        key_pn = types.InlineKeyboardButton(text='Понедельник', callback_data='pn')
        keyboard.add(key_pn)
        key_vt = types.InlineKeyboardButton(text='Вторник', callback_data='vt')
        keyboard.add(key_vt)
        key_sr = types.InlineKeyboardButton(text='Среда', callback_data='sr')
        keyboard.add(key_sr)
        key_ch = types.InlineKeyboardButton(text='Четверг', callback_data='ch')
        keyboard.add(key_ch)
        key_pt = types.InlineKeyboardButton(text='Пятница', callback_data='pt')
        keyboard.add(key_pt)
        key_sb = types.InlineKeyboardButton(text='Суббота', callback_data='sb')
        keyboard.add(key_sb)
        bot.send_message(message.from_user.id, text='Привет, на какой день тебе показать расписание?', reply_markup=keyboard)
    elif message.text == "/tomorrow":
        weekday = datetime.today().strftime('%A')
        if weekday == 'Sunday':
            keyboard = types.InlineKeyboardMarkup()
            key_pn = types.InlineKeyboardButton(text='Завтра (Понедельник)', callback_data='pn')
            keyboard.add(key_pn)
            bot.send_message(message.from_user.id, text='Расписание на:', reply_markup=keyboard)
        elif weekday == 'Monday':
            keyboard = types.InlineKeyboardMarkup()
            key_vt = types.InlineKeyboardButton(text='Завтра (Вторник)', callback_data='vt')
            keyboard.add(key_vt)
            bot.send_message(message.from_user.id, text='Расписание на:', reply_markup=keyboard)
        elif weekday == 'Tuesday':
            keyboard = types.InlineKeyboardMarkup()
            key_sr = types.InlineKeyboardButton(text='Завтра (Среда)', callback_data='sr')
            keyboard.add(key_sr)
            bot.send_message(message.from_user.id, text='Расписание на:', reply_markup=keyboard)
        elif weekday == 'Wednesday':
            keyboard = types.InlineKeyboardMarkup()
            key_ch = types.InlineKeyboardButton(text='Завтра (Четверг)', callback_data='ch')
            keyboard.add(key_ch)
            bot.send_message(message.from_user.id, text='Расписание на:', reply_markup=keyboard)
        elif weekday == 'Thursday':
            keyboard = types.InlineKeyboardMarkup()
            key_pt = types.InlineKeyboardButton(text='Завтра (Пятница)', callback_data='pt')
            keyboard.add(key_pt)
            bot.send_message(message.from_user.id, text='Расписание на:', reply_markup=keyboard)
        elif weekday == 'Friday':
            keyboard = types.InlineKeyboardMarkup()
            key_sb = types.InlineKeyboardButton(text='Завтра (Суббота)', callback_data='sb')
            keyboard.add(key_sb)
            bot.send_message(message.from_user.id, text='Расписание на:', reply_markup=keyboard)
        elif weekday == 'Saturday':
            keyboard = types.InlineKeyboardMarkup()
            key_pn = types.InlineKeyboardButton(text='Послезавтра (Понедельник)', callback_data='pn')
            keyboard.add(key_pn)
            bot.send_message(message.from_user.id, text='Расписание на:', reply_markup=keyboard)
    elif message.text == "/bells":
        f = open('zvonki.txt', 'r', encoding="utf-8")
        file_contents = f.read()
        print(file_contents)
        bot.send_message(message.from_user.id, file_contents)
        f.close()
    elif message.text == "/weather":
        url = 'https://www.accuweather.com/ru/ru/yurga/288372/current-weather/288372'
        agent = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=agent).text

        with open('weather.html', 'w') as output_file:
            output_file.write(r)

        with open("weather.html", "r") as f:
            contents = f.read()

            soup = BeautifulSoup(contents, 'lxml')

            for tag11 in soup.find_all("div", class_="card-header spaced-content", limit=1):
                for tag10 in soup.find_all("div", class_="content-module subnav-pagination"):
                    for tag in soup.find_all("div", class_="display-temp"):
                        with open('weather.html', 'w') as done:
                            tag11.insert(2, tag10.text)
                            tag11.insert(3, tag.text)
                            done.write(tag11.prettify())
        with open("weather.html", "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if '<div class="card-header spaced-content">' not in line:
                    if "<h1>" not in line:
                        if "Текущая погода" not in line:
                            if "</h1>" not in line:
                                if '<p class="sub">' not in line:
                                    if "</p>" not in line:
                                        if "</div>" not in line:
                                            f.write(line)
                                        f.truncate()
        with open("weather.html", "r+", encoding="utf-8") as f:
            f = open('weather.html', 'r')
            file_contents = f.read()
            print(file_contents)
            bot.send_message(message.from_user.id, file_contents)
            f.close()
    elif message.text == "/creator":
        bot.send_message(message.from_user.id, "Made By MrUDDoff (Денис)\n\nСтудент группы ИСиП-20")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Этот бот создан для группы ИСиП-20.\nДля удобства просмотра "
                                               "расписания на день недели, а так же расписания "
                                               "звоноков.\n\nКоманды:\n\n/bells - расписание звонков\n/zr - расписание "
                                               "дней\n/tomorrow - расписание на завтра\n\nBy MrUDDoff\nBot version v0.5")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # if call.data == "zvonki":
    #     f = open('zvonki.txt', 'r', encoding="utf-8")
    #     file_contents = f.read()
    #     bot.send_message(call.message.chat.id, file_contents)
    #     f.close()
    if call.data == "pn":
        try:
            url = 'http://utmiit.ru/ZR/ZR1.htm'
            r = requests.get(url)
            r.encoding = 'cp1251'

            with open('zr1.htm', 'w', encoding="windows-1251") as output_file:
                output_file.write(r.text)

            with open("zr1.htm", "r", encoding="windows-1251") as f:
                contents = f.read()

                soup = BeautifulSoup(contents, 'lxml')

                for tag10 in soup.find_all("td", colspan="9"):
                    for tag1 in soup.find("td", string="ИСиП-20"):
                        for tag in tag1.find_all_next(string=True, limit=16):
                            with open('zr1-result.htm', 'w', encoding="utf-8") as done:
                                tag10.append(tag.text)
                                done.write(tag10.prettify())
                            print(tag10.text)
            with open("zr1-result.htm", "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if '<td class="xl24" colspan="9">' not in line:
                        if '<span style="mso-spacerun:yes">' not in line:
                            if "</span>" not in line:
                                if "</td>" not in line:
                                    f.write(line)
                                f.truncate()
            f = open('zr1-result.htm', 'r', encoding="utf-8")
            file_contents = f.read()
            bot.send_message(call.message.chat.id, file_contents)
            f.close()
        except:
            bot.send_message(call.message.chat.id, "Error! Нас нет в расписании.")
    if call.data == "vt":
        try:
            url = 'http://utmiit.ru/ZR/ZR2.htm'
            r = requests.get(url)
            r.encoding = 'cp1251'

            with open('zr2.htm', 'w', encoding="windows-1251") as output_file:
                output_file.write(r.text)

            with open("zr2.htm", "r", encoding="windows-1251") as f:
                contents = f.read()

                soup = BeautifulSoup(contents, 'lxml')

                for tag10 in soup.find_all("td", colspan="9"):
                    for tag1 in soup.find("td", string="ИСиП-20"):
                        for tag in tag1.find_all_next(string=True, limit=16):
                            with open('zr2-result.htm', 'w', encoding="utf-8") as done:
                                tag10.append(tag.text)
                                done.write(tag10.prettify())
                            print(tag10.text)
            with open("zr2-result.htm", "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if '<td class="xl24" colspan="9">' not in line:
                        if '<span style="mso-spacerun:yes">' not in line:
                            if "</span>" not in line:
                                if "</td>" not in line:
                                    f.write(line)
                                f.truncate()
            f = open('zr2-result.htm', 'r', encoding="utf-8")
            file_contents = f.read()
            bot.send_message(call.message.chat.id, file_contents)
            f.close()
        except:
            bot.send_message(call.message.chat.id, "Error! Нас нет в расписании.")
    if call.data == "sr":
        try:
            url = 'http://utmiit.ru/ZR/ZR3.htm'
            r = requests.get(url)
            r.encoding = 'cp1251'

            with open('zr3.htm', 'w', encoding="windows-1251") as output_file:
                output_file.write(r.text)

            with open("zr3.htm", "r", encoding="windows-1251") as f:
                contents = f.read()

                soup = BeautifulSoup(contents, 'lxml')

                for tag10 in soup.find_all("td", colspan="9"):
                    for tag1 in soup.find("td", string="ИСиП-20"):
                        for tag in tag1.find_all_next(string=True, limit=16):
                            with open('zr3-result.htm', 'w', encoding="utf-8") as done:
                                tag10.append(tag.text)
                                done.write(tag10.prettify())
                            print(tag10.text)
            with open("zr3-result.htm", "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if '<td class="xl24" colspan="9">' not in line:
                        if '<span style="mso-spacerun:yes">' not in line:
                            if "</span>" not in line:
                                if "</td>" not in line:
                                    f.write(line)
                                f.truncate()
            f = open('zr3-result.htm', 'r', encoding="utf-8")
            file_contents = f.read()
            bot.send_message(call.message.chat.id, file_contents)
            f.close()
        except:
            bot.send_message(call.message.chat.id, "Error! Нас нет в расписании.")
    if call.data == "ch":
        try:
            url = 'http://utmiit.ru/ZR/ZR4.htm'
            r = requests.get(url)
            r.encoding = 'cp1251'

            with open('zr4.htm', 'w', encoding="windows-1251") as output_file:
                output_file.write(r.text)

            with open("zr4.htm", "r", encoding="windows-1251") as f:
                contents = f.read()

                soup = BeautifulSoup(contents, 'lxml')

                for tag10 in soup.find_all("td", colspan="9"):
                    for tag1 in soup.find("td", string="ИСиП-20"):
                        for tag in tag1.find_all_next(string=True, limit=16):
                            with open('zr4-result.htm', 'w', encoding="utf-8") as done:
                                tag10.append(tag.text)
                                done.write(tag10.prettify())
                            print(tag10.text)
            with open("zr4-result.htm", "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if '<td class="xl24" colspan="9">' not in line:
                        if '<span style="mso-spacerun:yes">' not in line:
                            if "</span>" not in line:
                                if "</td>" not in line:
                                    f.write(line)
                                f.truncate()
            f = open('zr4-result.htm', 'r', encoding="utf-8")
            file_contents = f.read()
            bot.send_message(call.message.chat.id, file_contents)
            f.close()
        except:
            bot.send_message(call.message.chat.id, "Error! Нас нет в расписании.")
    if call.data == "pt":
        try:
            url = 'http://utmiit.ru/ZR/ZR5.htm'
            r = requests.get(url)
            r.encoding = 'cp1251'

            with open('zr5.htm', 'w', encoding="windows-1251") as output_file:
                output_file.write(r.text)

            with open("zr5.htm", "r", encoding="windows-1251") as f:
                contents = f.read()

                soup = BeautifulSoup(contents, 'lxml')

                for tag10 in soup.find_all("td", colspan="9"):
                    for tag1 in soup.find("td", string="ИСиП-20"):
                        for tag in tag1.find_all_next(string=True, limit=16):
                            with open('zr5-result.htm', 'w', encoding="utf-8") as done:
                                tag10.append(tag.text)
                                done.write(tag10.prettify())
                            print(tag10.text)
            with open("zr5-result.htm", "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if '<td class="xl24" colspan="9">' not in line:
                        if '<span style="mso-spacerun:yes">' not in line:
                            if "</span>" not in line:
                                if "</td>" not in line:
                                    f.write(line)
                                f.truncate()
            f = open('zr5-result.htm', 'r', encoding="utf-8")
            file_contents = f.read()
            bot.send_message(call.message.chat.id, file_contents)
            f.close()
        except:
            bot.send_message(call.message.chat.id, "Error! Нас нет в расписании.")
    if call.data == "sb":
        try:
            url = 'http://utmiit.ru/ZR/ZR6.htm'
            r = requests.get(url)
            r.encoding = 'cp1251'

            with open('zr6.htm', 'w', encoding="windows-1251") as output_file:
                output_file.write(r.text)

            with open("zr6.htm", "r", encoding="windows-1251") as f:
                contents = f.read()

                soup = BeautifulSoup(contents, 'lxml')

                for tag10 in soup.find_all("td", colspan="9"):
                    for tag1 in soup.find("td", string="ИСиП-20"):
                        for tag in tag1.find_all_next(string=True, limit=16):
                            with open('zr6-result.htm', 'w', encoding="utf-8") as done:
                                tag10.append(tag.text)
                                done.write(tag10.prettify())
                            print(tag10.text)
            with open("zr6-result.htm", "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if '<td class="xl24" colspan="9">' not in line:
                        if '<span style="mso-spacerun:yes">' not in line:
                            if "</span>" not in line:
                                if "</td>" not in line:
                                    f.write(line)
                                f.truncate()
            f = open('zr6-result.htm', 'r', encoding="utf-8")
            file_contents = f.read()
            bot.send_message(call.message.chat.id, file_contents)
            f.close()
        except:
            bot.send_message(call.message.chat.id, "Error! Нас нет в расписании.")
bot.polling(none_stop=True, interval=0)
