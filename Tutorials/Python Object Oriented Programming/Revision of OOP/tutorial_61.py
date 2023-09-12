'''
Date 11-10-2021

In this tutorial you will learn about Multiple Inheritance in Classes
'''


class Person():
    def __init__(self, name=None, height=None, weight=None):
        self.name = name
        self.height = height
        self.weight = weight

    def print_details_of_person(self):
        print(
            f"Name is {self.name}\nHeight is {self.height} cm\nWeight is {self.weight} kg")


class Employee():
    number_of_leaves = 15
    salary = 100

    def __init__(self, number_of_leaves=None, salary=None):
        self.number_of_leaves = number_of_leaves
        self.salary = salary

    def print_details_of_employee(self):
        print(
            f"Salary is {self.salary} Rupees\nNumber of leaves left are {self.number_of_leaves}")

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave


class Programmer(Employee, Person):
    known_programming_language = []

    @staticmethod
    def static_method():
        print("I\'m a Static Method")

    def add_language(self, *lang):
        self.known_programming_language.extend(lang)

    def print_details_of_programmer(self):
        self.print_details_of_employee()
        print("Programmer knows the following languages--")
        for lang in self.known_programming_language:
            print(lang)


aman = Programmer(9, 87814)
aman.add_language(*["C++", "Python", "HTML", "JavaScript"])
aman.print_details_of_programmer()
