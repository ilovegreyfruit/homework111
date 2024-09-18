import sqlalchemy
from sqlalchemy.orm import sessionmaker
from classes import Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://login:password@localhost:5432/database'
engine = sqlalchemy.create_engine(DSN)

session = sessionmaker(bind=engine)
session = session()

def get_sales_by_publisher(publisher_name):
    results = (
    session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
    .join(Stock, Book.id == Stock.id_book)
    .join(Shop, Shop.id == Stock.id_shop)
    .join(Sale, Stock.id == Sale.id_stock)
    .join(Publisher, Publisher.id == Book.publusher_id)
    .filter(Publisher.name == publisher_name)
    .all()
    )
    for title, shop_name, price, date_sale in results:
        print(f"{title} | {shop_name} | {price} {date_sale}")
    if not results:
        print(f'Издатель "{publisher_name}" не найден.)
        return

publisher_name = input('Введите имя издателя: ')
get_sales_by_publisher(publisher_name)

session.close()