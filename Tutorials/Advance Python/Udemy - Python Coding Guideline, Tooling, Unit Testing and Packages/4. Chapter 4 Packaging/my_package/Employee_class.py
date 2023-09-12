'''
Date 10-11-2021

This code is part of a package created for a course

Note: This code is copied from my previous written code you can find that code from the below given GitHub link:
https://github.com/AmanRathoreM/All-in-Python/blob/11f8b50360a587ac133021cf6f87c445734e0a52/Tutorials/Python%20Object%20Oriented%20Programming/Revision%20of%20OOP/tutorial_70_2.py
'''

import typing


class Employee:
    number_of_leaves = 15
    name = "Unknown"
    salary = 100

    def __init__(self,  name="Unknown", salary=0.0, number_of_leaves=0):
        '''This is a constructor of class Employee which helps to manage Employees information

        Args:
            name (str, optional): Enter the name of the employee here. Defaults to "Unknown".
            salary (float, optional): Enter the salary of the employee here. Defaults to 0.0.
            number_of_leaves (int, optional): Enter the number of leaves taken by the employee here. Defaults to 0.

        Raises:
            Warning: If salary is not a float
        '''
        if not(isinstance(salary, float)):
            raise Warning('salary must be a float')
        self.number_of_leaves = int(number_of_leaves)
        self.name = name
        self.salary = float(salary)

    def print_details(self) -> None:
        '''Print all the details of the employee.
        '''
        print(
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}\nEmail is {self.return_email}")

    @property
    def return_email(self, mail: str = "gmail"):
        '''Returns email of the person 

        Args:
            mail (str, optional): enter the domain of the email. Defaults to "gmail".

        Returns:
            str: Full Email address of the person.
        '''

        if self.name == None:
            return "Email is not defined (You can set it using Setter)"
        return f"{self.name}@{mail}.com"

    @return_email.setter
    def return_email(self, email_address: str = "None@gmail.com"):
        if '@' not in email_address:
            raise ValueError("Not a valid email address")
        self.name = email_address.split('@')[0]

    @return_email.deleter
    def return_email(self):
        self.name = None

    @classmethod
    def change_leaves(cls, leave: int = 2):
        '''Changes the number of leaves employee has

        Args:
            leave (int, optional): Number of leaves employee will have after changing. Defaults to 2.
        '''
        cls.number_of_leaves = leave

    @classmethod
    def alternative_constructor_for_class(cls, employee_info: str, split_symbol='-'):
        return cls(*employee_info.split(split_symbol))

    def __add__(self, other) -> typing.SupportsFloat:
        '''adds the salary of 2 Employees

        Args:
            other (Employee object): object of the second person whose salary you want to add.

        Returns:
            float: Sum of the salaries of two employees.
        '''
        return f"Sum of {self.name}\'s and {other.name}\'s salary is {self.salary + other.salary}"

    def __matmul__(self, other):
        return f"2 * sum of {self.name}\'s and {other.name}\'s salary is {(self.salary + other.salary)*2}"

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}"

    def __repr__(self):
        return f"Employee(\"{self.name}\", {self.salary}, {self.number_of_leaves})"


if __name__ == "__main__":
    aman = Employee("Aman", 4000.0, 14)
    print(aman)
