class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Category.total_unique_products += 1

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Ошибка: цена введена некорректно.")
        else:
            self.__price = value

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            return NotImplemented


class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self._Category__products = None
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        product_list = ""
        for product in self.__products:
            product_list += str(product) + "\n"
        return product_list

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."


# Добавил пример работы классов
if __name__ == "__main__":
    # Создаем категорию и несколько товаров
    category = Category("Electronics", "Electronics category")
    laptop = Product("Laptop", "Laptop description", 1000.50, 10)
    phone = Product("Phone", "Phone description", 800.75, 20)

    # Добавляем товары в категорию
    category.add_product(laptop)
    category.add_product(phone)

    # Выводим информацию о категории и ее товарах
    print(category)
    print(category.products)

    total_value = laptop + phone
    print("Общая стоимость товаров:", total_value)