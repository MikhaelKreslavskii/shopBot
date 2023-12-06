from sqlalchemy.orm import Session

import models
import uuid

class Order:
    def __init__(self, user_id: int, stuff_id: int, count_stuff: int, session: Session):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.stuff_id = stuff_id
        self.count_stuff=count_stuff
        self.session = Session
    def create_order(self):
        order = models.OrdersModel(
            id= self.id,
            user_id=self.user_id,
            stuff_id=self.stuff_id,
            count_stuff=self.count_stuff

            )

        # with Session(engine) as session:
        #     with session.begin():
        #        # models.AbstractModel.metadata.create_all(engine)
        #         session.add(stuff)
        #         print(f"Add stuff to db {stuff}")
        #         session.commit()

        self.session.add(order)
        self.session.commit()
        self.session.close()




