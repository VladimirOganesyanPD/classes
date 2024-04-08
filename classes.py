class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self._Category__products = None
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут для списка товаров
        Category.total_categories += 1

    def add_product(self, product):
        """Метод для добавления товара в список товаров."""
        self.__products.append(product)

    @property
    def products(self):
        """Геттер для атрибута 'товары'."""
        product_list = ""
        for product in self.__products:
            product_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_list


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity
        Category.total_unique_products += 1

    @classmethod
    def create_product(cls, name, description, price, quantity):
        """Метод класса для создания товара."""
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для атрибута 'цена'."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для атрибута 'цена' с проверкой на корректность."""
        if value <= 0:
            print("Ошибка: цена введена некорректно.")
        else:
            self.__price = value
