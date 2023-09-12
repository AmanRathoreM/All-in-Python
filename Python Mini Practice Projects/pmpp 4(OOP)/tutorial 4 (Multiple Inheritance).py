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


class Player():
    number_of_games = 4

    def __init__(self, aname, game):
        self.name = aname
        self.game = game

    def printdetails(self):
        return f"The Name is {self.name}. \nGames are {self.game}."


class CoolProgrammer(Employee, Player):
    # def __init__(self, *args):
    #     super(CoolProgrammer, self).__init__(*args))
    language = ["C++", "Ruby"]

    def print_languages(self):
        return f"The Name is {self.name}. \nLanguages are {self.language}."


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")


suresh = Player("Suresh", ["Football", "Cricket", "Basketball"])


aman = CoolProgrammer("Aman", 8787, "Computer Scientest")
print(aman.print_languages())
