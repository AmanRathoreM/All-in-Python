'''
Date 12-10-2021

In this tutorial, you will learn about Dunder Methods
You can see the python documentation for more information of diffrent types of dunder methods
and to get to the documentation just search "mapping operators to function in python"
'''


class Employee:
    number_of_leaves = 15
    name = "Unknown"
    salary = 100

    def __init__(self,  name, salary, number_of_leaves):
        self.number_of_leaves = int(number_of_leaves)
        self.name = name
        self.salary = int(salary)

    def print_details(self):
        print(
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}")

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave

    @classmethod
    def alternative_constructor_for_class(cls, str, split_symbol='-'):
        return cls(*str.split(split_symbol))

    def __add__(self, other):
        return f"Sum of {self.name}\'s and {other.name}\'s salary is {self.salary + other.salary}"

    def __matmul__(self, other):
        return f"2 * sum of {self.name}\'s and {other.name}\'s salary is {(self.salary + other.salary)*2}"

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}"

    def __repr__(self):
        return f"Employee(\"{self.name}\", {self.salary}, {self.number_of_leaves})"


aman = Employee("Aman", 100, 11)
rohan = Employee.alternative_constructor_for_class("Rohan-200-54")

# print(aman+rohan)
# print(aman @ rohan)
print(rohan, "\n\n")
print(repr(rohan))
