from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from telebot import types

import models
from Admin import Admin

from Bot_singleton import BotSingleton
from Catalog import Catalog
from Order import Order
from Stuff import Stuff
from User import User
from creating_db import create_db, Session
import json

# from Catalog import Catalog
# from User import User


# from creating_stuffs import creating_stuffs
# from creating_user import creating_user


bot = BotSingleton()

create_db()

admin = Admin()
catalog = Catalog(session=Session())


#admin.creating_stuffs(Session())


@bot.message_handler(commands=['start'])
def start(message):
    # if message.text == '/start':
    user = User(message=message)
    user.add_user_to_db(session=Session())
    #
    #     bot.send_message(message.from_user.id,
    #                      f'Приветствую тебя {user.name} {user.fullname}. Чтобы посмотреть каталог продуктов нажмите /cat. Чтобы купить товар, введи его порядковый номер')
    #
    # elif message.text == '/cat':
    #     bot.register_next_step_handler(message, show_catalog)
    #
    # if message.text.isdigit():
    #
    #     if (int(message.text) > len(catalog.stuffs)) or (int(message.text) < 0):
    #         bot.send_message(message.from_user.id, "Такого номера нет в списке")
    #     else:
    #         bot.register_next_step_handler(message, make_order)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bin_btn = types.KeyboardButton("Каталог")
    cat_btn = types.KeyboardButton("Корзина")
    markup.add(bin_btn, cat_btn)
    bot.send_message(message.chat.id, text=f"Привет, {user.name} {user.fullname} ! У меня ты можешь сделать заказ",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def button_responce(message):
    if (message.text == "Каталог"):
        catalog = Catalog(session=Session())
        stuffs = catalog.get_stuffs()
        print(stuffs)
        # i = 1
        keyboard = types.InlineKeyboardMarkup()
        count=0
        for stuff in stuffs:
            if int(stuff.count)<=0:
                continue
            button_stuff = types.InlineKeyboardButton(f'{stuff.name}',
                                                      callback_data=str(f'{stuff.id}\n') + stuff.description + str(
                                                          f'\n Цена: {stuff.price} \nКоличество: {stuff.count}'))
            print("suc")
            keyboard.add(button_stuff)
            count+=1
        if count == 0:
            bot.send_message(message.from_user.id, text="Товары кончились, заходите позже")
        else:
            bot.send_message(message.from_user.id, reply_markup=keyboard, text="Список имеющихся товаров")

    else:
        # bot.send_message(message.from_user.id, text="На данный момент товаров в корзине нет")
        orders = Session().query(models.OrdersModel).all()
        print(f'My orders {orders}')
        print(len(orders))
        if len(orders) == 0:
            bot.send_message(message.from_user.id, text="В корзине ничего нет")
        else:
            res_str=''
            for order in orders:
                # if int(order.stuff.count)<0:
                #     continue
                res_str=res_str+order.stuff.name+'\n'
            bot.send_message(message.from_user.id, text=str(f"Ваши товары: \n {res_str}"))



# def make_order(message):
#     print(f'AAAAAAA {message.text}')
#
#     bot.send_message(message.from_user.id, "Введите количество товара")
#     cur_stuff = catalog.get_stuffs()[int(message.text)]
#     print(type(cur_stuff))
#     if not message.text.isdigit():
#         bot.send_message(message.from_user.id, "Пожалуйста, введите количество товара")
#     elif cur_stuff.count < int(message.text):
#         bot.send_message(message.from_user.id, "У меня столько нет(")
#     else:
#         ###ДОБАВИТЬ ДОБАВЛЕНИЕ ЗАКАЗА
#         ...


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        print(call.data)
    global cur_stuff_id
    global cur_user_id
    cur_stuff_id = int(call.data.partition('\n')[0])

    cur_user_id = call.message.from_user.id
    result = call.data.split('\n', 1)[1:]
    my_btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
    take_btn = types.KeyboardButton("Беру")
    back_btn = types.KeyboardButton("Назад")
    my_btns.add(take_btn, back_btn)

    bot.send_message(chat_id=call.message.chat.id, reply_markup=my_btns, text=result)
    bot.register_next_step_handler(call.message, take_back_button)


@bot.message_handler(commands=['button'])
def take_back_button(message):
    if message.text == "Назад":

        ...

    else:

        order = Order(user_id=cur_user_id, stuff_id=cur_stuff_id, count_stuff=1, )
        order.create_order(session=Session())
        bot.send_message(message.from_user.id, text="Товар добавлен в корзину")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bin_btn = types.KeyboardButton("Каталог")
    cat_btn = types.KeyboardButton("Корзина")
    markup.add(bin_btn, cat_btn)
    bot.send_message(chat_id=message.chat.id, reply_markup=markup,
                     text="Чтобы посмотреть товары, выбери Каталог. Чтобы посмотреть свою корзину, выбери Корзина")
    bot.register_next_step_handler(message, button_responce)

bot.polling(none_stop=True, interval=0)
