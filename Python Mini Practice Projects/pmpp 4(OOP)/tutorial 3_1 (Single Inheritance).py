# Date 29-06-2021

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def static_function_to_print_a_string(string="This is a String"):
        print(string)


class Programer(Employee):
    def languages(self, language):
        self.language = language


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

karan = Programer("Karan", "454578", "Student")
karan.languages("C++")

print("Karan language is", karan.language)
print("Karan salary is", karan.salary)
