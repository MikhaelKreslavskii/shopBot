from sqlalchemy.orm import Session

import models



### класс пользователя тг
class User:
    def __init__(self, message):
        self.id = message.from_user.id
        self.name = message.from_user.first_name
        self.fullname = message.from_user.last_name

    ### добавление пользователя в базу данных
    def add_user_to_db(self, session: Session):
        user = models.UserModel(
            name=self.name,
            fullname=self.fullname,
            user_id=self.id)

        # models.AbstractModel.metadata.create_all(engine)
        session.add(user)
        session.commit()
