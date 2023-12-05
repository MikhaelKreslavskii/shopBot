from sqlalchemy.orm import Session

import models


class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


### каталог товаров
class Catalog(Singleton):
    def __init__(self):
        with Session(models.engine) as session:
            with session.begin():
                self.stuffs = session.query(models.StuffsModel).all()
                print(f"In catalog {self.stuffs}")
                #session.close()

    def get_stuffs(self):
        return self.stuffs
