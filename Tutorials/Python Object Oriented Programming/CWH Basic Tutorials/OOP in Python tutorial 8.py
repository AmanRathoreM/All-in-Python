# Date 29-3-2021

class Employe:

    def __init__(self, firstname, lastname, salary, contactnumber):
        self.fname = firstname
        self.lname = lastname
        self.salary = salary
        self.contactnumber = contactnumber

    def __mul__(self,other):
        """__add__ is a dunder method this method is used for addition"""
        return int(self.salary)+int(other.salary)

    def __repr__(self):
        return "First Name ----> {}\nLast Name ----> {}\nSalary ----> {}\nContact Number ----> {}\n".format(self.fname,self.lname,self.salary,self.contactnumber)

    def __str__(self):
        return "The name of the Employe is ----> {}".format(self.fname)

rohan = Employe("Rohan", "Das", "104389", "9872642157")
harry = Employe("Harry", "Johnson", "170890", "9874521683")

# print(rohan+harry)
print(repr(harry))
# print(str(harry))