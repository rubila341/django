from database import session
from models import Product, Category

def add_example_data():
    # Create new categories
    electronics = Category(name='Electronics', description='Devices and gadgets')
    groceries = Category(name='Groceries', description='Food and beverages')

    # Add categories to session
    session.add(electronics)
    session.add(groceries)
    session.commit()

    # Create new products
    smartphone = Product(name='Smartphone', price=299.99, in_stock=True, category_id=electronics.id)
    laptop = Product(name='Laptop', price=799.99, in_stock=True, category_id=electronics.id)
    milk = Product(name='Milk', price=1.99, in_stock=True, category_id=groceries.id)
    bread = Product(name='Bread', price=1.29, in_stock=True, category_id=groceries.id)
    apples = Product(name='Apples', price=2.50, in_stock=True, category_id=groceries.id)

    # Add products to session
    session.add(smartphone)
    session.add(laptop)
    session.add(milk)
    session.add(bread)
    session.add(apples)
    session.commit()

if __name__ == "__main__":
    add_example_data()
    products = session.query(Product).all()
    for product in products:
        print(f"Product: {product.name}, Price: {product.price}")
