# * Date 10-10-2021

'''
* In this tutorial you will learn about Class Methods
'''


class Employee:
    number_of_leaves = 15
    name = "Unknown"
    salary = 100

    def __init__(self,  name="Unknown", salary=100, number_of_leaves=15):
        self.number_of_leaves = number_of_leaves
        self.name = name
        self.salary = salary

    def print_details(self):
        print(
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}")

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave


aman = Employee("Aman", 5487, 11)
rohan = Employee("Rohan", 123447)

rohan.change_leaves(96)

aman.print_details()
print(Employee.__dict__)
