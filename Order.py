from sqlalchemy.orm import Session

import models
import uuid


class Order:
    def __init__(self, user_id: int, stuff_id: int, count_stuff: int, ):
        # self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.stuff_id = stuff_id
        self.count_stuff = count_stuff

    def create_order(self, session: Session):
        order = models.OrdersModel(
            # id= self.id,
            user_id=self.user_id,
            stuff_id=self.stuff_id,
            count_stuff=self.count_stuff

        )

        session.query(models.StuffsModel).filter(models.StuffsModel.id == self.stuff_id).update(
        {'count': models.StuffsModel.count - self.count_stuff})
        #stuffs= session.query(models.StuffsModel).all()
        # for stuff in stuffs:
        #     if int(stuff.count)<=0:
        #         session.query(models.StuffsModel).filter(models.StuffsModel.id==stuff.id).delete()




        session.add(order)
        session.commit()
        session.close()
