import time
import telebot
from telebot import types
import os
import win10toast
from mss import mss
from rich import print
from rich.console import Console
import auto
import Internet

console = Console()


def main():
    console.clear()
    try:
        f = open(os.getenv('APPDATA') + 'TurnOffBot\\token', 'r')
        f.close()
    except IOError and Exception:
        auto.auto()

    ff = open(os.getenv('APPDATA') + 'TurnOffBot\\token', 'r')
    token = ff.read()
    ff.close()

    turn_on = False

    while not turn_on:
        try:
            Internet.main()

            print('Made by rus152')
            print('')

            bot = telebot.TeleBot(token)

            print('Бот в данный момент ОнЛайн')

            @bot.message_handler(commands=['start'])
            def send_welcome(message):
                bot.send_message(message.chat.id, 'Я НАГИБАТОР3000, только напиши и комп отключится')
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                but1 = types.KeyboardButton("/shutdown")
                but2 = types.KeyboardButton("/Online")
                but3 = types.KeyboardButton("/hibernation")
                but5 = types.KeyboardButton("/Screen")
                but6 = types.KeyboardButton("/lock🔒")
                but4 = types.KeyboardButton("/cancel")
                markup.add(but1, but2, but3, but5, but6, but4)
                bot.reply_to(message, "Вывод кнопок", parse_mode='html', reply_markup=markup)

            @bot.message_handler(commands=['hibernation'])
            def send(message):
                bot.reply_to(message, "Комп переходит в режим гибернация", )
                os.system('shutdown /h')

            @bot.message_handler(commands=['lock🔒'])
            def send(message):
                bot.reply_to(message, "Блокировка компа 🔒", )
                os.system('rundll32.exe user32.dll, LockWorkStation')

            @bot.message_handler(commands=['shutdown'])
            def send(message):
                sec = types.ReplyKeyboardMarkup(resize_keyboard=True)
                but0 = types.KeyboardButton("0")
                but1 = types.KeyboardButton("1800")
                but2 = types.KeyboardButton("3600")
                but3 = types.KeyboardButton("7200")
                but4 = types.KeyboardButton("21600")
                but5 = types.KeyboardButton("Назад")
                sec.add(but0, but1, but2, but3, but4, but5)
                msg: str = bot.send_message(message.chat.id, 'Через сколько отключить компьютер?(В секундах)',
                                            parse_mode='html', reply_markup=sec)
                bot.register_next_step_handler(msg, test)

            def test(message):
                txt = message.text
                print(txt)

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                but1 = types.KeyboardButton("/shutdown")
                but2 = types.KeyboardButton("/Online")
                but3 = types.KeyboardButton("/hibernation")
                but5 = types.KeyboardButton("/Screen")
                but6 = types.KeyboardButton("/lock🔒")
                but4 = types.KeyboardButton("/cancel")
                markup.add(but1, but2, but3, but5, but6, but4)

                if txt == "Назад":
                    bot.reply_to(message, "Возврат", parse_mode='html', reply_markup=markup)
                    return

                try:
                    if int(txt) >= 18000:
                        cas = int(txt) / 3600
                        print(cas)
                        bot.reply_to(message, "Компьютер выключится через " + str(round(int(cas))) + " часов 🕑",
                                     parse_mode='html',
                                     reply_markup=markup)

                    if (int(txt) >= 7200) and (int(txt) < 18000):
                        cas = int(txt) / 3600
                        print(cas)
                        bot.reply_to(message, "Компьютер выключится через " + str(round(int(cas))) + " часа 🕑",
                                     parse_mode='html',
                                     reply_markup=markup)

                    if (int(txt) > 3599) and (int(txt) < 7200):
                        cas = int(txt) / 3600
                        print(cas)
                        bot.reply_to(message, "Компьютер выключится через " + str(round(int(cas))) + " час 🕑",
                                     parse_mode='html',
                                     reply_markup=markup)

                    if (int(txt) > 60) and (int(txt) < 120):
                        menu = int(txt) / 60
                        print(menu)
                        bot.reply_to(message, "Компьютер выключится через " + str(round(int(menu))) + " минуту 🕑",
                                     parse_mode='html',
                                     reply_markup=markup)

                    if (int(txt) > 119) and (int(txt) < 300):
                        menu = int(txt) / 60
                        print(menu)
                        bot.reply_to(message, "Компьютер выключится через " + str(round(int(menu))) + " минуты 🕑",
                                     parse_mode='html',
                                     reply_markup=markup)

                    if (int(txt) > 299) and (int(txt) < 3600):
                        menu = int(txt) / 60
                        print(menu)
                        bot.reply_to(message, "Компьютер выключится через " + str(round(int(menu))) + " минут 🕑",
                                     parse_mode='html',
                                     reply_markup=markup)

                    if (int(txt) > 0) and (int(txt) < 61):
                        menu = int(txt) / 60
                        print(menu)
                        bot.reply_to(message, "Компьютер выключится через " + txt + " секунд 🕑", parse_mode='html',
                                     reply_markup=markup)

                    if int(txt) == 0:
                        bot.reply_to(message, "Компьютер отключается ", parse_mode='html',
                                     reply_markup=markup)
                    os.system('shutdown /s /t ' + txt)

                except Exception as _ex:
                    bot.reply_to(message,
                                 str(_ex),
                                 parse_mode='html',
                                 reply_markup=markup)
                    return

            @bot.message_handler(commands=['cancel'])
            def send(message):
                bot.reply_to(message, "Отключение отменено", )
                os.system('shutdown /a')

            @bot.message_handler(commands=['Online'])
            def send(message):
                bot.reply_to(message, "В данный момент комп онлайн", )
                toaster = win10toast.ToastNotifier()
                toaster.show_toast("БОТЯРА 🔔", "Все знают, что комп онлайн", icon_path="icon.ico")

            @bot.message_handler(commands=['Screen'])
            def send(message):
                bot.reply_to(message, "Запрос отправлен", )
                mss().shot(mon=1)
                try:
                    mss().shot(mon=2)
                except Exception as _ex:
                    print(_ex)
                toaster = win10toast.ToastNotifier()
                toaster.show_toast("БОТЯРА 🔔", "Запрос на скриншот", icon_path="icon.ico")
                bot.send_message(message.chat.id, 'Скриншот сделан')
                bot.send_document(message.chat.id, document=open('monitor-1.png', 'rb'))
                try:
                    bot.send_document(message.chat.id, document=open('monitor-2.png', 'rb'))
                except Exception as _ex:
                    print(_ex)
                os.remove('monitor-1.png')
                try:
                    os.remove('monitor-2.png')
                except Exception as _ex:
                    print(_ex)

            bot.polling(none_stop=True)
        except Exception as ex:
            print("Произошла ошибка, попытка перезапуска", ex)
            time.sleep(5)
            console.clear()


if __name__ == '__main__':
    main()
