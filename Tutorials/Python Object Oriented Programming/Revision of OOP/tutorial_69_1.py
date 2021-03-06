'''
Date 12-10-2021

In this tutorial, you will learn about Setters, and property Decorators
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
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}\nEmail is {self.return_email}")

    @property
    def return_email(self, mail="gmail"):
        return f"{self.name}@{mail}.com"

    @return_email.setter
    def return_email(self, email_address="None@gmail.com"):
        if '@' not in email_address:
            raise ValueError("Not a valid email address")
        try:
            self.name = email_address.split('@')[0]
        except print(0):
            print("Error while setting name")

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


aman = Employee("Aman", 4000, 14)
# aman.print_details()
print(aman.return_email)
aman.return_email = "Aman0864@gmail.com"
print(aman.return_email, "\n")
aman.print_details()
# print(aman._Employee__return_email())
