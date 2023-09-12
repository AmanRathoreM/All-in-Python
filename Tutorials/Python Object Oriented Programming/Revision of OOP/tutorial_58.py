'''
Date 11-10-2021

In this tutorial you will learn about Static methods on Classes
Static methods are those arguments which takes no self as an argument
'''


class Employee:
    number_of_leaves = 15
    name = "Unknown"
    salary = 100

    def __init__(self,  name, salary, number_of_leaves):
        self.number_of_leaves = number_of_leaves
        self.name = name
        self.salary = salary

    def print_details(self):
        print(
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}")

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave

    @classmethod
    def alternative_constructor_for_class(cls, str, split_symbol='-'):
        return cls(*str.split(split_symbol))

    @staticmethod
    def static_method():
        print("I\'m a Static Method")


aman = Employee("Aman", 5487, 11)
rohan = Employee.alternative_constructor_for_class("Rohan-123447-54")


rohan.static_method()
