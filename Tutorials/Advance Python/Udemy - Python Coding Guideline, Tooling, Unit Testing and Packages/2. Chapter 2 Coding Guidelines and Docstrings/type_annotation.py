'''
Date 10-11-2021

In this tutorial, you will learn about Docstrings in Sphinx style
'''


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

    def print_details(self):
        print(
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}\nEmail is {self.return_email}")

    @property
    def return_email(self, mail: str = "gmail") -> str:
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

    def __str__(self) -> str:
        return f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}"


aman = Employee("Aman", 4000.1, 14)
# rohit = Employee("Rohit", 4000, 14)

print(aman.return_email)
print(aman)
