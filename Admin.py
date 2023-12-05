from sqlalchemy.orm import Session

from Stuff import Stuff


class Admin:
    # def __init__(self):
    #     ...

    def creating_stuffs(self, session:Session):
        for i in range(2):
            name = input("Enter name of stuff")
            category = input("Enter category of staff")
            description = input("Enter description of staff")
            count = input("Enter count of stuffs")
            price = input("Enter price of stuff")
            stuff = Stuff(name=name, category=category, description=description, count=count, price=price)
            stuff.add_to_db(session=session)
            print("add")
