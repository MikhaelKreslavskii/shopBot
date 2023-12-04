from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory", echo=True)
with engine.connect() as connection:
    result  = connection.execute(text("select 'hello world'"))

    print(result.scalars().all())