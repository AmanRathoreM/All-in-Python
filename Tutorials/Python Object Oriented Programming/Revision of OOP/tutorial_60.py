'''
Date 11-10-2021

In this tutorial you will learn about Single Inheritance in Classes
'''


class Person():
    def __init__(self, name=None, height=None, weight=None):
        self.name = name
        self.height = height
        self.weight = weight

    def print_details_of_person(self):
        print(
            f"Name is {self.name}\nHeight is {self.height} cm\nWeight is {self.weight} kg")

    @staticmethod
    def static_method():
        print("I\'m a Static Method")


class Employee(Person):
    number_of_leaves = 15
    salary = 100

    def __init__(self, name=None, height=None, weight=None, number_of_leaves=None, salary=None):
        self.name = name
        self.height = height
        self.weight = weight
        self.number_of_leaves = number_of_leaves
        self.salary = salary

    def print_details_of_employee(self):
        self.print_details_of_person()
        print(
            f"Salary is {self.salary} Rupees\nNumber of leaves left are {self.number_of_leaves}")

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave


# aman = Employee("Aman", 26, 161)
aman = Employee(5698, 11)
aman.print_details_of_employee()
# aman.static_method()
rohan = Person("Rohan", 56, 170)
rohan.print_details_of_person()

# rohan.static_method()
