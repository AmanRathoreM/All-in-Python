# Date 28-3-2021

class Employe:
    increment = 1.378546
    # So, salary will be = present salary * increment
    number_of_Employe = 0

    def __init__(self, firstname, lastname, salary, contactnumber):
        self.fname = firstname
        self.lname = lastname
        self.salary = salary
        self.contactnumber = contactnumber
        Employe.number_of_Employe = Employe.number_of_Employe+1
        # To increase employes as soon as the def __init__ function execute

    def increase(self):
        self.salary = int(self.salary) * self.increment

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount


rohan = Employe("Rohan", "Das", "120000", "9872642157")
harry = Employe("Harry", "Johnson", "120000", "9874521683")

print("Harry salary before incremeant.\n", harry.salary)
harry.increase()
print("Harry salary after incremeant.\n", harry.salary)

print(5*"\n")

print("Harry salary before incremeant change.\n", harry.salary)
Employe.change_increment(4)
harry.increase()
print("Harry salary after incremeant change.\n", harry.salary)

# print(Employe.number_of_Employe)
# print(rohan.fname, harry.fname)
