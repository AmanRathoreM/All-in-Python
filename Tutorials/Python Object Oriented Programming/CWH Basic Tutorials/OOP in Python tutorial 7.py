# Date 29-3-2021

class Employe:

    def __init__(self, firstname, lastname, salary, contactnumber):
        self.fname = firstname
        self.lname = lastname
        self.salary = salary
        self.contactnumber = contactnumber


class Programmer(Employe):
    # This is an Inherictance class
    def __init__(self, firstname, lastname, salary, contactnumber, experience, language):
        super().__init__(firstname, lastname, salary, contactnumber)
        # super() is used to call properties of the parent class into it's child class
        self.language = experience
        self.language = language


rohan = Employe("Rohan", "Das", "120000", "9872642157")
harry = Employe("Harry", "Johnson", "120000", "9874521683")
aman = Programmer("Aman", "Rathore", "300000", "8003479539",
                  "0 Years", "Python, Html, Css, JavaScript, C, C++, Arduino")

print(aman.__dict__)
