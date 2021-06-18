# Date 29-3-2021

class Employe:

    def __init__(self, firstname, lastname, salary, contactnumber):
        self.fname = firstname
        self.lname = lastname
        self.salary = salary
        self.contactnumber = contactnumber

    @classmethod
    def from_str(cls, employe_data):
        """This is an Alternative Constructer for class Employe"""
        fname, lname, salary, contactnumber = employe_data.split("-")
        return cls(fname, lname, salary, contactnumber)

    @staticmethod
    def holiday(day):
        if (day != "Sunday"):
            return False 
        else:
            return True


rohan = Employe.from_str("Rohan-Das-120000-9872642157")
harry = Employe.from_str("Harry-Johnson-120000-9874521683")
aman = Employe.from_str("Aman-Rathore-300000-8003479539")

# print(rohan.__dict__)

print(Employe.holiday("Monday"))


# print("Harry salary before incremeant.\n", harry.salary)
# harry.increase()
# print("Harry salary after incremeant.\n", harry.salary)

# print(5*"\n")

# print("Harry salary before incremeant change.\n", harry.salary)
# Employe.change_increment(4)
# harry.increase()
# print("Harry salary after incremeant change.\n", harry.salary)


# print(Employe.number_of_Employe)
# print(rohan.fname, harry.fname)
