import pytest

from classes import Category, Product, AbstractProduct, Smartphone, Grass


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


# След. два теста(прайс сеттер и метод продукта работают некорректно , не понимаю почему. Я написал как смог.
def test_price_setter():
    product = Product("Laptop", "Laptop description", 1000.50, 10)
    original_price = product.price
    product.price = -500
    assert product.price == original_price


def test_str_method_product():
    product = Product("Laptop", "Laptop description", 1000.50, 10)
    expected_output = "Laptop, 1000.50 руб. Остаток: 10 шт."
    assert str(product) == expected_output


def test_add_method_product():
    product1 = Product("Laptop", "Laptop description", 1000.50, 10)
    product2 = Product("Phone", "Phone description", 800.75, 20)
    with pytest.raises(TypeError):
        total_value = product1 + product2


def test_smartphone_creation():
    smartphone = Smartphone("Smartphone", "Smartphone description", 1000.50, 10, "High", "Model X", "128GB", "Black")
    assert isinstance(smartphone, AbstractProduct)


def test_grass_creation():
    grass = Grass("Grass", "Grass description", 10.75, 100, "Russia", "14 days", "Green")
    assert isinstance(grass, AbstractProduct)


def test_some_common_method(setup_products):
    product1, _ = setup_products
    assert product1.some_common_method() is None  # Просто проверяем, что метод работает без ошибок