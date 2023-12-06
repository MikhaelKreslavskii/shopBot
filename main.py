from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Admin import Admin

from Bot_singleton import BotSingleton
from Catalog import Catalog
from Stuff import Stuff
from User import User
from creating_db import create_db, Session

# from Catalog import Catalog
# from User import User


# from creating_stuffs import creating_stuffs
# from creating_user import creating_user


bot = BotSingleton()

create_db()

admin = Admin()
catalog = Catalog(session=Session())
admin.creating_stuffs(Session())


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        user = User(message=message)
        user.add_user_to_db(session=Session())

        bot.send_message(message.from_user.id,
                         f'Приветствую тебя {user.name} {user.fullname}. Чтобы посмотреть каталог продуктов нажмите /cat. Чтобы купить товар, введи его порядковый номер')

    elif message.text == '/cat':
        bot.register_next_step_handler(message, show_catalog)

    if message.text.isdigit():

        if (int(message.text) > len(catalog.stuffs)) or (int(message.text) < 0):
            bot.send_message(message.from_user.id, "Такого номера нет в списке")
        else:
            bot.register_next_step_handler(message, make_order)


def show_catalog(message):
    stuffs = catalog.get_stuffs()
    i = 1
    for stuff in stuffs:
        bot.send_message(message.from_user.id, f'{i}:{stuff.name} - {stuff.price}. Осталось: {stuff.count}')
        i += 1


# print(stuffs)


def make_order(message):
    print(f'AAAAAAA {message.text}')
    bot.send_message(message.from_user.id, "Введите количество товара")
    cur_stuff = catalog.get_stuffs()[int(message.text)]
    print(type(cur_stuff))
    if not message.text.isdigit():
        bot.send_message(message.from_user.id, "Пожалуйста, введите количество товара")
    elif cur_stuff.count < int(message.text):
        bot.send_message(message.from_user.id, "У меня столько нет(")
    else:
        ###ДОБАВИТЬ ДОБАВЛЕНИЕ ЗАКАЗА
        ...


bot.polling(none_stop=True, interval=0)
