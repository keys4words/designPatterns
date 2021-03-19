from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    "A Hypothetical Class Interface (Product)"

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method"

class ConreteProductA(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductA"

    def create_object(self):
        return self


class ConreteProductB(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductB"

    def create_object(self):
        return self


class ConreteProductC(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductC"

    def create_object(self):
        return self

class Creator:
    "The Factory Class"
    @staticmethod
    def create_object(some_property):
        "A static method to get a conrete product"
        if some_property == 'a':
            return ConreteProductA()
        if some_property == 'b':
            return ConreteProductB()
        if some_property == 'c':
            return ConreteProductC()
        return None


# client
product = Creator().create_object('b')
print(product.name)