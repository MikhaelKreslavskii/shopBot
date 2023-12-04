from sqlalchemy import select
from sqlalchemy.orm import Session

import models
from sqlalchemy.orm import  Session
def creating_stuffs():

    for i in range(2):
        name=input("Enter name of stuff")
        category = input("Enter category of staff")
        description = input("Enter description of staff")
        count = input("Enter count of stuffs")
        price=input("Enter price of stuff")

        stuff = models.StuffsModel(
            name=name,
            category=category,
            description=description,
            count= count,
            price=price)

        with Session(models.engine) as session:
             with session.begin():
                    models.AbstractModel.metadata.create_all(models.engine)
                    session.add(stuff)
                    #session.close()




creating_stuffs()

with Session(models.engine) as session:
    with session.begin():
       stuffs = session.query(models.StuffsModel).all()


       for stuff in stuffs:
            print(f'name - {stuff.name} and price - {stuff.price}')