from sqlalchemy.orm import Session

import models
from Stuff import Stuff


# class Singleton(object):
#     _instance = None
#
#     def __new__(class_, *args, **kwargs):
#         if not isinstance(class_._instance, class_):
#             class_._instance = object.__new__(class_, *args, **kwargs)
#         return class_._instance
#

### каталог товаров
class Catalog(object):
    def __init__(self, session: Session):
        self.stuffs = session.query(models.StuffsModel).all()
        print(f"In catalog {self.stuffs}")

    def get_stuffs(self) -> list[Stuff]:
        return self.stuffs
