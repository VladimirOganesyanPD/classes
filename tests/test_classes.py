import pytest

from classes import Category, Product


@pytest.fixture
def setup_categories():
    category1 = Category("Electronics", "Electronics category")
    category2 = Category("Books", "Books category")
    return category1, category2


@pytest.fixture
def setup_products():
    product1 = Product("Laptop", "Laptop description", 1000.50, 10)
    product2 = Product("Book", "Book description", 20.99, 50)
    return product1, product2


def test_add_product():
    category = Category("Electronics", "Electronics category")
    product = Product("Laptop", "Laptop description", 1000.50, 10)
    category.add_product(product)
    assert len(category._Category__products) == 1


def test_product_list_format(setup_categories, setup_products):
    category1, _ = setup_categories
    product1, _ = setup_products

    category1.add_product(product1)
    expected_output = f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт.\n"
    assert category1.products == expected_output


def test_create_product():
    product = Product.create_product("Laptop", "Laptop description", 1000.50, 10)
    assert product.name == "Laptop"
    assert product.description == "Laptop description"
    assert product.price == 1000.50
    assert product.quantity == 10


def test_price_setter():
    product = Product("Laptop", "Laptop description", 1000.50, 10)
    product.price = -500  # Пытаемся установить некорректную цену
    assert product.price == 1000.50  # Цена не изменилась из-за некорректного ввода