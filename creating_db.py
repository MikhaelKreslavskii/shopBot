from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import models

DATABASE_NAME = 'shopData.sqlite'
engine=create_engine(f'sqlite:///{DATABASE_NAME}',echo=True)
Session = sessionmaker(bind=engine)

def create_db():
    print("Create db")
    models.AbstractModel.metadata.create_all(engine)