from abc import ABC, abstractmethod


class CreationInfoMixin:
    def __repr__(self):
        attrs = ', '.join(f"{attr}={getattr(self, attr)!r}" for attr in self.__dict__)
        return f"{type(self).__name__}({attrs})"


class AbstractProduct(ABC, CreationInfoMixin):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        print(f"Object of class {type(self).__name__} created with attributes:")
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

    @abstractmethod
    def some_common_method(self):
        pass

    def increase_quantity(self, amount):
        self.quantity += amount

    def decrease_quantity(self, amount):
        self.quantity -= amount


class Product(AbstractProduct):
    def some_common_method(self):
        pass

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def some_common_method(self):
        pass

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. Performance: {self.performance}, Model: {self.model}, Memory: {self.memory}, Color: {self.color}"


class Grass(Product):
    def __init__(self, name, description, price, quantity, country, sprouting_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.sprouting_period = sprouting_period
        self.color = color

    def some_common_method(self):
        pass

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. Country: {self.country}, Sprouting Period: {self.sprouting_period}, Color: {self.color}"


class Category:
    total_categories = 0

    def __init__(self, name, description):
        self.__products = []
        self.name = name
        self.description = description
        Category.total_categories += 1
        print(f"Object of class {type(self).__name__} created with attributes:")
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

    def add_product(self, product):
        if not isinstance(product, AbstractProduct):
            raise TypeError("Можно добавлять только объекты типа AbstractProduct или его наследники.")
        self.__products.append(product)

    @property
    def products(self):
        product_list = ""
        for product in self.__products:
            product_list += str(product) + "\n"
        return product_list

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."


if __name__ == "__main__":
    category = Category("Electronics", "Electronics category")
    smartphone = Smartphone("Smartphone", "Smartphone description", 1000.50, 10, "High", "Model X", "128GB", "Black")
    grass = Grass("Grass", "Grass description", 10.75, 100, "Russia", "14 days", "Green")

    category.add_product(smartphone)
    category.add_product(grass)

    print(category)
    print(category.products)