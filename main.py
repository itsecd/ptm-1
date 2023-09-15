from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from aiogram.types.message import ContentType
from telebot import types


TOKEN = "5550601778:AAEcLnx-UCf4sjlMyJOA-7L3-aAulTNQlWo"
TOKEN_PAY = "1877036958:TEST:5995ac386bfd73a83b8f5fb2000e335213a0d345"
VAL = "RUB"
THIS_GROUP = ""
PRICE_LITE = types.LabeledPrice(label='BOX1', amount=72500)
PRICE_PRO = types.LabeledPrice(label='BOX2', amount=120000)
KROSS1 = 'https://ae04.alicdn.com/kf/H9c79f950267c4f3497b6510042f98d8az/-.jpg'
PRO_PHOTO = 'https://drive.google.com/file/d/1GpAOLZ5XCVqqh4o_Hb_Mt0hYBnHnXIkH/view?usp=share_link'
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message) -> None:
    """
        Функция начала работы бота
        :message: - объект сообщения
    """
    panel = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton('💳Оплатить покупку (online) (1с)')
    btn_2 = types.KeyboardButton('💵Оплатить покупку (через представителя) (24ч)')
    btn_3 = types.KeyboardButton('⁉️Информация')
    panel.add(btn_1, btn_2, btn_3)
    await bot.send_message(message.chat.id,
                           '📌Приветствую!\nЯ бот 💳BoxPay и я помогу оплатить любые покупки в интернете! '
                           'Перейди в раздел ⁉️Информация если тебе что то не понятно по оплате покупок!',
                           reply_markup=panel)


@dp.message_handler(content_types=["text"])
async def text(message) -> None:
    """
        Функция обрабатывает текст отправленный пользователем (отслеживание события нажатия на кнопку)
        :message: - объект сообщения
    """
    if message.text == '⁉️Информация':
        panel = types.ReplyKeyboardMarkup(resize_keyboard=True)
        await bot.send_message(message.chat.id,
                               '''📌Раздел информации об оплате покупки.\nBoxPay - бот через который происходит оплата 
                               любой покупки. Есть два типа оплаты:\n   1. 💳Оплатить покупку (online) - это оплата 
                               через онлайн платежную систему, платеж занимает всего навсего 1 секунду 
                               ( быстро и надежно ).
                         \n   2. 💵Оплатить покупку (через представителя) - если вы боитесь оплачивать через бота 
                         ( или нам не доверяете ), тогда эта оплата для вас, но она занимает времени от 24 часов до 48 
                         часов. Вам будет отправлена ссылка на нашего представителя и он поможет вам с оплатой!
                         \n\n Когда я смогу увидеть свою покупку?\nСразу после оплаты мы отправим товар на указанный 
                         вами адрес!
                         \n\n Я могу оплатить курс где угодно? Из любой точки мира?\n Да, совершенно верно! Вы можете
                          оплатите покупку из любой точки мира!''',
                               reply_markup=panel)
    elif message.text == '💵Оплатить покупку (через представителя) (24ч)':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("🇺🇸🇬🇧🇷🇺Andrey", url='https://t.me/andreyko777')
        button2 = types.InlineKeyboardButton("🇺🇸🇬🇧🇷🇺Dmitriy", url='https://t.me/andreyko777')
        button3 = types.InlineKeyboardButton("🇬🇧🇷🇺Alexandra", url='https://t.me/andreyko777')
        button4 = types.InlineKeyboardButton("🇬🇧🇷🇺Daria", url='https://t.me/andreyko777')
        button5 = types.InlineKeyboardButton("🇺🇸🇬🇧🇷🇺Daniil", url='https://t.me/andreyko777')
        button6 = types.InlineKeyboardButton("🇬🇧🇷🇺Sergei", url='https://t.me/andreyko777')
        button7 = types.InlineKeyboardButton("🇺🇸🇬🇧Tommy", url='https://t.me/andreyko777')
        button8 = types.InlineKeyboardButton("🇺🇸🇬🇧Angelo", url='https://t.me/andreyko777')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
        await bot.send_message(message.chat.id,
                               '''🚨Выберите представителя BoxPay🚨''',
                               reply_markup=markup)
    elif message.text == '💳Оплатить покупку (online) (1с)':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("💵USD🇺🇸", callback_data="1")
        button2 = types.InlineKeyboardButton("💶EUR🇪🇺", callback_data='2')
        button3 = types.InlineKeyboardButton("💷AED🇦🇪", callback_data='3')
        button4 = types.InlineKeyboardButton("💴CNY🇨🇳", callback_data='4')
        button5 = types.InlineKeyboardButton("💎RUB🇷🇺", callback_data='5')
        markup.add(button1, button2, button3, button4, button5)
        await bot.send_message(message.chat.id,
                               '''✅Выберите валюту для оплаты✅''',
                               reply_markup=markup)
    elif message.text == '1':
        panel = types.ReplyKeyboardMarkup(resize_keyboard=True)
        await bot.send_message(message.chat.id,
                               '''test''',
                               reply_markup=panel)
    else:
        panel = types.ReplyKeyboardMarkup(resize_keyboard=True)
        await bot.send_message(message.chat.id,
                               '''❌К сожалению я не знаю такой команды❌''',
                               reply_markup=panel)


@dp.callback_query_handler(lambda c: c.data)
async def answer(call: types.CallbackQuery) -> None:
    """
        Функция обрабатывает кнопку нажатую пользователем через callback
        dp.callback_query_handler() - декоратор
        :call: - обработчик callback
    """
    global VAL
    global THIS_GROUP
    if call.data == '1':
        VAL = "USD"
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("🧨BOX1🧨", callback_data='11')
        button2 = types.InlineKeyboardButton("🔥BOX2🔥", callback_data='22')
        markup.add(button1, button2)
        await bot.send_message(call.message.chat.id, '''✅(USD)Выберите покупку BoxPay✅''', reply_markup=markup)
    if call.data == '2':
        VAL = "EUR"
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("🧨BOX1🧨", callback_data='11')
        button2 = types.InlineKeyboardButton("🔥BOX2🔥", callback_data='22')
        markup.add(button1, button2)
        await bot.send_message(call.message.chat.id, '''✅(EUR)Выберите покупку BoxPay✅''', reply_markup=markup)
    if call.data == '3':
        VAL = "AED"
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("🧨BOX1🧨", callback_data='11')
        button2 = types.InlineKeyboardButton("🔥BOX2🔥", callback_data='22')
        markup.add(button1, button2)
        await bot.send_message(call.message.chat.id, '''✅(AED)Выберите покупку BoxPay✅''', reply_markup=markup)
    if call.data == '4':
        VAL = "CNY"
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("🧨BOX1🧨", callback_data='11')
        button2 = types.InlineKeyboardButton("🔥BOX2🔥", callback_data='22')
        markup.add(button1, button2)
        await bot.send_message(call.message.chat.id, '''✅(CNY)Выберите покупку BoxPay✅''', reply_markup=markup)
    if call.data == '5':
        VAL = "RUB"
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("🧨BOX1🧨", callback_data='11')
        button2 = types.InlineKeyboardButton("🔥BOX2🔥", callback_data='22')
        markup.add(button1, button2)
        await bot.send_message(call.message.chat.id, '''✅(RUB)Выберите покупку BoxPay✅''', reply_markup=markup)
    if call.data == '11':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("Pay", pay=True))
        if VAL == 'USD':
            THIS_GROUP = "BOX1"
            await bot.send_invoice(call.message.chat.id,
                                   title='Оплата покупки BoxPay (BOX1)',
                                   description='кроссовки BOX1',
                                   provider_token=TOKEN_PAY,
                                   currency='USD',
                                   photo_url=KROSS1,
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   need_phone_number=False,
                                   need_email=False,
                                   is_flexible=False,
                                   prices=[types.LabeledPrice(label='кроссовки BOX1', amount=int(2250 / 71 * 100))],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload", reply_markup=keyboard)
        if VAL == 'RUB':
            THIS_GROUP = "BOX1"
            await bot.send_invoice(call.message.chat.id,
                                   title='Оплата покупки BoxPay (BOX1)',
                                   description='кроссовки BOX1',
                                   provider_token=TOKEN_PAY,
                                   currency='RUB',
                                   photo_url=KROSS1,
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   need_phone_number=False,
                                   need_email=False,
                                   is_flexible=False,
                                   prices=[types.LabeledPrice(label='кроссовки BOX1', amount=int(232500))],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload", reply_markup=keyboard)
        if VAL == 'AED':
            THIS_GROUP = "BOX1"
            await bot.send_invoice(call.message.chat.id,
                                   title='Оплата покупки BoxPay (BOX1)',
                                   description='кроссовки BOX1',
                                   provider_token=TOKEN_PAY,
                                   currency='AED',
                                   photo_url=KROSS1,
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   need_phone_number=False,
                                   need_email=False,
                                   is_flexible=False,
                                   prices=[types.LabeledPrice(label='кроссовки BOX1', amount=int(2250 * 0.0505 * 100))],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload", reply_markup=keyboard)
        if VAL == 'EUR':
            THIS_GROUP = "BOX1"
            await bot.send_invoice(call.message.chat.id,
                                   title='Оплата покупки BoxPay (BOX1)',
                                   description='кроссовки BOX1',
                                   provider_token=TOKEN_PAY,
                                   currency='EUR',
                                   photo_url=KROSS1,
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   need_phone_number=False,
                                   need_email=False,
                                   is_flexible=False,
                                   prices=[types.LabeledPrice(label='кроссовки BOX1', amount=int(2250 / 76 * 100))],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload", reply_markup=keyboard)
        if VAL == 'CNY':
            THIS_GROUP = "BOX1"
            await bot.send_invoice(call.message.chat.id,
                                   title='Оплата покупки BoxPay (BOX1)',
                                   description='кроссовки BOX1',
                                   provider_token=TOKEN_PAY,
                                   currency='CNY',
                                   photo_url=KROSS1,
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   need_phone_number=False,
                                   need_email=False,
                                   is_flexible=False,
                                   prices=[types.LabeledPrice(label='кроссовки BOX1', amount=int(2250 / 10.2 * 100))],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload", reply_markup=keyboard)
    if call.data == '22':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("Pay", pay=True))
        if VAL == 'USD':
            THIS_GROUP = "BOX2"
            await bot.send_invoice(call.message.chat.id,
                                   title='Оплата покупки BoxPay (BOX2)',
                                   description='кроссовки BOX2',
                                   provider_token=TOKEN_PAY,
                                   currency='USD',
                                   photo_url=KROSS1,
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   need_phone_number=False,
                                   need_email=False,
                                   is_flexible=False,
                                   prices=[types.LabeledPrice(label='кроссовки BOX2', amount=int(4700 / 71 * 100))],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload", reply_markup=keyboard)
        if VAL == 'RUB':
            THIS_GROUP = "BOX2"
            await bot.send_invoice(call.message.chat.id,
                                   title='Оплата покупки BoxPay (BOX2)',
                                   description='кроссовки BOX2',
                                   provider_token=TOKEN_PAY,
                                   currency='RUB',
                                   photo_url=KROSS1,
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   need_phone_number=False,
                                   need_email=False,
                                   is_flexible=False,
                                   prices=[types.LabeledPrice(label='кроссовки BOX2', amount=int(480000))],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload", reply_markup=keyboard)
        if VAL == 'AED':
            THIS_GROUP = "BOX2"
            await bot.send_invoice(call.message.chat.id,
                                   title='Оплата покупки BoxPay (BOX2)',
                                   description='кроссовки BOX2',
                                   provider_token=TOKEN_PAY,
                                   currency='AED',
                                   photo_url=KROSS1,
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   need_phone_number=False,
                                   need_email=False,
                                   is_flexible=False,
                                   prices=[types.LabeledPrice(label='кроссовки BOX2', amount=int(4700 * 0.0505 * 100))],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload", reply_markup=keyboard)
        if VAL == 'EUR':
            THIS_GROUP = "BOX2"
            await bot.send_invoice(call.message.chat.id,
                                   title='Оплата покупки BoxPay (BOX2)',
                                   description='кроссовки BOX2',
                                   provider_token=TOKEN_PAY,
                                   currency='EUR',
                                   photo_url=KROSS1,
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   need_phone_number=False,
                                   need_email=False,
                                   is_flexible=False,
                                   prices=[types.LabeledPrice(label='кроссовки BOX2', amount=int(4700 / 76 * 100))],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload", reply_markup=keyboard)
        if VAL == 'CNY':
            THIS_GROUP = "BOX2"
            await bot.send_invoice(call.message.chat.id,
                                   title='Оплата покупки BoxPay (BOX2)',
                                   description='кроссовки BOX2',
                                   provider_token=TOKEN_PAY,
                                   currency='CNY',
                                   photo_url=KROSS1,
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   need_phone_number=False,
                                   need_email=False,
                                   is_flexible=False,
                                   prices=[types.LabeledPrice(label='кроссовки BOX2', amount=int(4700 / 11.4 * 100))],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload", reply_markup=keyboard)


@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery) -> None:
    """
        Функия обработки запроса на checkid
        :pre_checkout_q: - объект запроса
    """
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message) -> None:
    """
        Функция удачной оплаты
        :message: - объект сообщения
    """
    global THIS_GROUP
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
    await bot.send_message(message.chat.id,
                           f"Платёж на сумму {message.successful_payment.total_amount // 100} "
                           f"{message.successful_payment.currency} прошел успешно!!!")
    if THIS_GROUP == "LITE":
        await bot.send_message(message.chat.id,
                               f"""📲Поздравляю вы оплатили кроссовки BOX1!\nВот несколько простых шагов, что нужно 
                               делать дальше: 
                               \n\n   1. ✅Ожидайте уведомление от продавца (он сообщит когда ваши кроссовки прибудут)
                               \n   2. ✅После уведомления о прибытии кроссовок у вас есть ровно 5 дней чтобы забрать 
                               их с указанной почты.
                               """)
    if THIS_GROUP == "PRO":
        await bot.send_message(message.chat.id,
                               f"""📲Поздравляю вы оплатили кроссовки BOX2!\nВот несколько простых шагов, что нужно 
                               делать дальше: 
                               \n\n   1. ✅Ожидайте уведомление от продавца (он сообщит когда ваши кроссовки прибудут).
                               \n   2. ✅После уведомления о прибытии кроссовок у вас есть ровно 5 дней чтобы забрать 
                               их с указанной почты.
                               """)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
