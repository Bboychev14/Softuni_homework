from abc import ABC, abstractmethod

from demo_project.core_1.validator_1 import Validator


class BakedFood(ABC):
    @abstractmethod
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_null_or_whitespace(value, "Name cannot be empty string or white space!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_if_number_is_zero_or_negative(value, "Price cannot be less than or equal to zero!")
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"