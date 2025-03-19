import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Word


def create_db(engine):
    words = (
        ('Bagel', 'Бублик'),
        ('Breakfast', 'Завтрак'),
        ('Dinner', 'Ужин'),
        ('House', 'Дом'),
        ('Cat', 'Кот'),
        ('Dog', 'Собака'),
        ('Pink', 'Розовый'),
        ('White', 'Белый'),
        ('Beatiful', 'Красивый'),
        ('Friend', 'Друг')
    )
    create_tables(engine)

    for i in words:
        session.add(Word(word=i[0], translate=i[1]))
    session.commit()

engine = sqlalchemy.create_engine('postgresql://postgres:'password'@localhost:5432/tgbot')
Session = sessionmaker(bind=engine)
session = Session()

create_db(engine)

session.close()
