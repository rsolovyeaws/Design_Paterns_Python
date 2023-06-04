from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    """Abstract class interface"""
    @staticmethod
    @abstractmethod
    def create_object():
        """Abstract method each concrete product should implement."""

class ConcreteProductA(IProduct):
    """Concrete Product A"""
    def __init__(self):
        self.name = "Concrete Product A"

    def create_object(self):
        return self

class ConcreteProductB(IProduct):
    """Concrete Product B"""
    def __init__(self):
        self.name = "Concrete Product B"

    def create_object(self):
        return self

class ConcreteProductC(IProduct):
    """Concrete Product C"""
    def __init__(self):
        self.name = "Concrete Product C"

    def create_object(self):
        return self

class Creator():
    """Factory class. Instantiates ConcreteProducts based on the property passed to the constructor"""
    
    @staticmethod
    def create_object(some_property):
        if some_property == 'a':
            return ConcreteProductA()
        
        if some_property == 'b':
            return ConcreteProductB()
        
        if some_property == 'c':
            return ConcreteProductC()

        return None

product = Creator.create_object('a')
print(product.name)
product = Creator.create_object('b')
print(product.name)
product = Creator.create_object('c')
print(product.name)
