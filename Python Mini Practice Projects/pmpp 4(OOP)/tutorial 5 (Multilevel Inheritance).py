# Date 29-06-2021

class Dad:
    baketball = 1


class Son(Dad):
    dance = 1
    baketball = 9

    def dancer(self):
        return f"Yes I dance {self.dance} times"


class Grand_son(Son):
    dance = 6

    def dancer(self):
        return f"Yes I dance good {self.dance} times"


'''
harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")


suresh = Player("Suresh", ["Football", "Cricket", "Basketball"])


aman = CoolProgrammer("Aman", 8787, "Computer Scientest")
print(aman.print_languages())
'''


arrai = Dad()
brrai = Son()
crrai = Grand_son()

print(crrai.baketball)
