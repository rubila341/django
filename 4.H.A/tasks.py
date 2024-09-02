from sqlalchemy import func
from models import Category, Product
from database import get_session


def populate_data():
    session = get_session()

    categories = [
        Category(name="Электроника", description="Гаджеты и устройства."),
        Category(name="Книги", description="Печатные книги и электронные книги."),
        Category(name="Одежда", description="Одежда для мужчин и женщин.")
    ]
    session.add_all(categories)
    session.commit()

    electronics = session.query(Category).filter_by(name="Электроника").first()
    books = session.query(Category).filter_by(name="Книги").first()
    clothing = session.query(Category).filter_by(name="Одежда").first()

    products = [
        Product(name="Смартфон", price=299.99, in_stock=True, category=electronics),
        Product(name="Ноутбук", price=499.99, in_stock=True, category=electronics),
        Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category=books),
        Product(name="Джинсы", price=40.50, in_stock=True, category=clothing),
        Product(name="Футболка", price=20.00, in_stock=True, category=clothing)
    ]
    session.add_all(products)
    session.commit()


def read_data():
    session = get_session()
    categories = session.query(Category).all()
    for category in categories:
        print(f"Категория: {category.name}, Описание: {category.description}")
        for product in category.products:
            print(f"  Продукт: {product.name}, Цена: {product.price}")


def update_data():
    session = get_session()
    product = session.query(Product).filter_by(name="Смартфон").first()
    if product:
        product.price = 349.99
        session.commit()


def aggregate_data():
    session = get_session()
    results = session.query(Category.name, func.count(Product.id)).join(Product).group_by(Category.id).all()
    for category_name, product_count in results:
        print(f"Категория: {category_name}, Количество продуктов: {product_count}")


def filter_categories():
    session = get_session()
    results = session.query(Category).join(Product).group_by(Category.id).having(func.count(Product.id) > 1).all()
    for category in results:
        print(f"Категория: {category.name}, Описание: {category.description}")
