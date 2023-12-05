from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import models
from Admin import Admin

from Bot_singleton import BotSingleton
from Catalog import Catalog
from User import User


# from creating_stuffs import creating_stuffs
# from creating_user import creating_user


bot = BotSingleton()






admin = Admin()

admin.creating_stuffs(Session())


# @bot.message_handler(content_types=['text'])
# def start(message):
#     user=User(message=message)
#     user.add_user_to_db()
#
#     bot.send_message(message.from_user.id,
#                      f'Приветствую тебя {user.name} {user.fullname}. Чтобы посмотреть каталог продуктов нажмите /cat')
#
#     if message.text == '/cat':
#         bot.register_next_step_handler(message, show_catalog)
#
#
# def show_catalog(message):
#     catalog = Catalog()
#     stuffs = catalog.get_stuffs()
#     print(stuffs)
#
#
#
#
# bot.polling(none_stop=True, interval=0)

