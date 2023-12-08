from sqlalchemy.orm import Session

import models
import uuid

###класс товара
class Stuff:
    def __init__(self, name: str, category: str, description: str, price: int, count: int):
        # self.id = str(uuid.uuid4())
        # print(type(self.id))
        self.name = name
        self.category = category
        self.description = description
        self.price = price
        self.count = count

   ### метод добавления товара в бд
    def add_to_db(self, session: Session):
        stuff = models.StuffsModel(
            #id=self.id,
            name=self.name,
            category=self.category,
            description=self.description,
            count=self.count,
            price=self.price)

        # with Session(engine) as session:
        #     with session.begin():
        #        # models.AbstractModel.metadata.create_all(engine)
        #         session.add(stuff)
        #         print(f"Add stuff to db {stuff}")
        #         session.commit()


        session.add(stuff)
        session.commit()
        session.close()
            # with session.begin():
            #     self.stuffs = session.query(models.StuffsModel).all()
            #     print(f"In catalog Stuff {self.stuffs}")

            #session.close()
