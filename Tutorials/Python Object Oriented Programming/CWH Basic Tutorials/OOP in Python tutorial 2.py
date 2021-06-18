# Date 22-3-2021

class Employe:
    def __init__(self, firstname, lastname, salary, contactnumber):
        self.fname = firstname
        self.lname = lastname
        self.salary = salary
        self.contactnumber = contactnumber


rohan = Employe("Rohan", "Das", "120000", "9872642157")
harry = Employe("Harry", "Johnson", "120000", "9874521683")


print(rohan.fname,harry.fname)  