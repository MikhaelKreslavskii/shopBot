import telebot
from sqlalchemy.orm import Session
from telebot import types
import models


def creating_user():
    bot = telebot.TeleBot('6728698451:AAGKVYgAFRGo0EQSZRCh2-A_EnNY_BbjQg0')

    @bot.message_handler(content_types=['text'])
    def start(message):
        user = models.UserModel(
            name=message.from_user.first_name,
            fullname = message.from_user.last_name,
            user_id = message.from_user.id)
        with Session(models.engine) as session:
            with session.begin():
                models.AbstractModel.metadata.create_all(models.engine)
                session.add(user)

                #session.close()
                #session.expunge(user)
            with session.begin():
                users = session.query(models.UserModel).all()
                print(users)

                for user in users:
                    print(f'name - {user.name} and price - {user.user_id}')
                session.close()

        bot.send_message(message.from_user.id, f'Приветствую тебя {user.name} {user.fullname}. Чтобы посмотреть каталог продуктов нажмите /cat')




    bot.polling(none_stop=True, interval=0)



creating_user()




