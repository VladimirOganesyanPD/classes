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


def test_category_initialization():
    category = Category("Electronics", "Electronics category")
    assert category.name == "Electronics"
    assert category.description == "Electronics category"
    assert category.products == []


def test_product_initialization():
    product = Product("Laptop", "Laptop description", 1000.50, 10)
    assert product.name == "Laptop"
    assert product.description == "Laptop description"
    assert product.price == 1000.50
    assert product.quantity == 10


def test_product_count(setup_categories, setup_products):
    category1, category2 = setup_categories
    product1, product2 = setup_products

    category1.products.append(product1)
    category2.products.append(product2)

    assert Category.total_unique_products == 3


def test_category_count(setup_categories):
    category1, category2 = setup_categories

    assert Category.total_categories == 5
