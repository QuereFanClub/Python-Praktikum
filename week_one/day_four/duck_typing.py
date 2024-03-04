class Product:
    def __init__(self, price, count):
        self._price = price
        self._count = count

    def price(self):
        return self._price

    def count(self):
        return self._count

    def add(self, n):
        self._count += n

    def ship(self, n):
        self._count -= n

    def setPrice(self, newprice):
        self._price = newprice


class Book(Product):
    def __init__(self, author, title, price, count):
        super().__init__(price, count)
        self._author = author
        self._title = title

    def author(self):
        return self._author

    def title(self):
        return self._title


class Computer(Product):
    def __init__(self, brand, model, processor, ram, price, count):
        super().__init__(price, count)
        self._brand = brand
        self._model = model
        self._processor = processor
        self._ram = ram

    def brand(self):
        return self._brand

    def model(self):
        return self._model

    def processor(self):
        return self._processor

    def ram(self):
        return self._ram
