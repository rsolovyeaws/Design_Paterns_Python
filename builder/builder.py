""" 
    Product can consist of A, B, C (Product is a list of parts) 
        Use Case:
            I want: 
                Product to have (A, C)
            I call: 
                Director's static method returns Product 
                by calling the Builder's static methods that construct the product by adding parts 
"""

from abc import ABCMeta, abstractmethod

class Product():
    """
    The instance of a product  :  
        Consists of one or more parts - list of parts
        Builder appends parts to the list
    """
    def __init__(self):
        self.parts = []

class IBuilder(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def build_part_a():
        """Builds part a of the object"""
    @staticmethod
    @abstractmethod
    def build_part_b():
        """Builds part a of the object"""
    @staticmethod
    @abstractmethod
    def build_part_c():
        """Builds part a of the object"""
    @staticmethod
    @abstractmethod
    def get_result():
        """Return the final object"""

class Builder(IBuilder):
    """ Builder class 

    returns product, build of different parts.
    Simple: 
        it has a list of parts:
            by request builder adds parts to the product
            returns a list of parts
    """
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append('a')
        return self

    def build_part_b(self):
        self.product.parts.append('b')
        return self

    def build_part_c(self):
        self.product.parts.append('c')
        return self
    
    def get_result(self):
        return self.product
    
class Director():

    @staticmethod
    def construct():
        return Builder().build_part_a().build_part_c().get_result()

ac_product = Director.construct()

print(ac_product.parts)
    