class Product:
    total_unique_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.total_unique_products += 1

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
        if not isinstance(other, Product):
            raise TypeError("Нельзя складывать продукты разных классов.")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class Grass(Product):
    def __init__(self, name, description, price, quantity, country, sprouting_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.sprouting_period = sprouting_period
        self.color = color


class Category:
    total_categories = 0

    def __init__(self, name, description):
        self._Category__products = []
        self.name = name
        self.description = description
        Category.total_categories += 1

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product или его наследники.")
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
    smartphone = Smartphone("Smartphone", "Smartphone description", 1000.50, 10, "High", "Model X", "128GB", "Black")
    grass = Grass("Grass", "Grass description", 10.75, 100, "Russia", "14 days", "Green")

    # Добавляем товары в категорию
    category.add_product(smartphone)
    category.add_product(grass)

    # Выводим информацию о категории и ее товарах
    print(category)
    print(category.products)

    # Проверяем функционал сложения
    total_value = smartphone + grass
    print("Общая стоимость товаров:", total_value)