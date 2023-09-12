# * Date 10-10-2021

'''
* In this tutorial you will learn about Class's instance variables
'''


class Employee:
    number_of_leaves = 15


aman = Employee()
rohan = Employee()
aman.name = "Aman"
rohan.name = "Rohan"
aman.salary = 548778
rohan.salary = 5878

# print(aman.name, aman.salary, rohan.name, rohan.salary)
# print(aman.number_of_leaves, rohan.number_of_leaves, Employee.number_of_leaves)
# aman.number_of_leaves = 3
# Employee.number_of_leaves += 1
# print(aman.number_of_leaves, rohan.number_of_leaves, Employee.number_of_leaves)

print(aman.__dict__)
print(rohan.__dict__)
print(Employee.__dict__)
