# <h1 style="text-align:center; font-size:360%; font-family:verdana;color:#4A3E76;"><em>Python Object Oriented Programming</em></h1>

# These _Object Oriented Programming_ tutorials are watched from [CodeWithHarry](https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww) YouTube Channel's [Python Playlist's](https://youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME) [Tutorial number 52](https://www.youtube.com/watch?v=o6zPAzl4ZtM&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=54) to [Tutorial number 70](https://www.youtube.com/watch?v=h1CmrQBAifY&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=72).

---

---

---

---

---

## **_1.) tutorial_52 of Python_**

### [**_Click me_**](tutorial_52.py "Clike here to see full file") to see full file of tutorial_52

```C++
'''
Date 10-10-2021

In this tutorial you will learn about introduction to OOP in Python
Use of Object Oriented Programming helps us work along with DRY principal
'''

print("Hello!")

```

---

---

## **_2.) tutorial_53 of Python_**

### [**_Click me_**](tutorial_53.py "Clike here to see full file") to see full file of tutorial_53

```C++
'''
Date 10-10-2021

In this tutorial you will learn how to create a simple class
'''


class Student:
    pass


aman = Student()
rohan = Student()
aman.name = "Aman"
rohan.name = "Rohan"

print(aman.name, rohan.name)
# print(aman, rohan)

```

---

---

## **_3.) tutorial_54 of Python_**

### [**_Click me_**](tutorial_54.py "Clike here to see full file") to see full file of tutorial_54

```C++
'''
Date 10-10-2021

In this tutorial you will learn about Class's instance variables
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

```

---

---

## **_4.) tutorial_55 of Python_**

### [**_Click me_**](tutorial_55.py "Clike here to see full file") to see full file of tutorial_55

```C++
'''
Date 10-10-2021

In this tutorial you will learn about Self and __init__() function
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


aman = Employee("Aman", 5487, 11)
rohan = Employee("Rohan", 123447)


aman.print_details()

```

---

---

## **_5.) tutorial_56 of Python_**

### [**_Click me_**](tutorial_56.py "Clike here to see full file") to see full file of tutorial_56

```C++
'''
Date 10-10-2021

In this tutorial you will learn about Class Methods
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

```

---

---

## **_6.) tutorial_57 of Python_**

### [**_Click me_**](tutorial_57.py "Clike here to see full file") to see full file of tutorial_57

```C++
'''
Date 11-10-2021

In this tutorial you will learn about how to use class method as an Alternative Constructors
'''


class Employee:
    number_of_leaves = 15
    name = "Unknown"
    salary = 100

    def __init__(self,  name, salary, number_of_leaves):
        self.number_of_leaves = number_of_leaves
        self.name = name
        self.salary = salary

    def print_details(self):
        print(
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}")

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave

    @classmethod
    def alternative_constructor_for_class(cls, str, split_symbol='-'):
        return cls(*str.split(split_symbol))


aman = Employee("Aman", 5487, 11)
rohan = Employee.alternative_constructor_for_class("Rohan-123447-54")


aman.print_details()
rohan.print_details()

```

---

---

## **_7.) tutorial_58 of Python_**

### [**_Click me_**](tutorial_58.py "Clike here to see full file") to see full file of tutorial_58

```C++
'''
Date 11-10-2021

In this tutorial you will learn about Static methods on Classes
Static methods are those arguments which takes no self as an argument
'''


class Employee:
    number_of_leaves = 15
    name = "Unknown"
    salary = 100

    def __init__(self,  name, salary, number_of_leaves):
        self.number_of_leaves = number_of_leaves
        self.name = name
        self.salary = salary

    def print_details(self):
        print(
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}")

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave

    @classmethod
    def alternative_constructor_for_class(cls, str, split_symbol='-'):
        return cls(*str.split(split_symbol))

    @staticmethod
    def static_method():
        print("I\'m a Static Method")


aman = Employee("Aman", 5487, 11)
rohan = Employee.alternative_constructor_for_class("Rohan-123447-54")


rohan.static_method()

```

---

---

## **_8.) tutorial_59 of Python_**

### [**_Click me_**](tutorial_59.py "Clike here to see full file") to see full file of tutorial_59

```C++
'''
Date 11-10-2021

In this tutorial you will learn about Abstraction and Encapsulation in Classes
'''

print("Hello!")

```

---

---

## **_9.) tutorial_60 of Python_**

### [**_Click me_**](tutorial_60.py "Clike here to see full file") to see full file of tutorial_60

```C++
'''
Date 11-10-2021

In this tutorial you will learn about Single Inheritance in Classes
'''


class Person():
    def __init__(self, name=None, height=None, weight=None):
        self.name = name
        self.height = height
        self.weight = weight

    def print_details_of_person(self):
        print(
            f"Name is {self.name}\nHeight is {self.height} cm\nWeight is {self.weight} kg")

    @staticmethod
    def static_method():
        print("I\'m a Static Method")


class Employee(Person):
    number_of_leaves = 15
    salary = 100

    def __init__(self, name=None, height=None, weight=None, number_of_leaves=None, salary=None):
        self.name = name
        self.height = height
        self.weight = weight
        self.number_of_leaves = number_of_leaves
        self.salary = salary

    def print_details_of_employee(self):
        self.print_details_of_person()
        print(
            f"Salary is {self.salary} Rupees\nNumber of leaves left are {self.number_of_leaves}")

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave


# aman = Employee("Aman", 26, 161)
aman = Employee(5698, 11)
aman.print_details_of_employee()
# aman.static_method()
rohan = Person("Rohan", 56, 170)
rohan.print_details_of_person()

# rohan.static_method()

```

---

---

## **_10.) tutorial_61 of Python_**

### [**_Click me_**](tutorial_61.py "Clike here to see full file") to see full file of tutorial_61

```C++
'''
Date 11-10-2021

In this tutorial you will learn about Multiple Inheritance in Classes
'''


class Person():
    def __init__(self, name=None, height=None, weight=None):
        self.name = name
        self.height = height
        self.weight = weight

    def print_details_of_person(self):
        print(
            f"Name is {self.name}\nHeight is {self.height} cm\nWeight is {self.weight} kg")


class Employee():
    number_of_leaves = 15
    salary = 100

    def __init__(self, number_of_leaves=None, salary=None):
        self.number_of_leaves = number_of_leaves
        self.salary = salary

    def print_details_of_employee(self):
        print(
            f"Salary is {self.salary} Rupees\nNumber of leaves left are {self.number_of_leaves}")

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave


class Programmer(Employee, Person):
    known_programming_language = []

    @staticmethod
    def static_method():
        print("I\'m a Static Method")

    def add_language(self, *lang):
        self.known_programming_language.extend(lang)

    def print_details_of_programmer(self):
        self.print_details_of_employee()
        print("Programmer knows the following languages--")
        for lang in self.known_programming_language:
            print(lang)


aman = Programmer(9, 87814)
aman.add_language(*["C++", "Python", "HTML", "JavaScript"])
aman.print_details_of_programmer()

```

---

---

## **_11.) tutorial_62_1 of Python_**

### [**_Click me_**](tutorial_62_1.py "Clike here to see full file") to see full file of tutorial_62_1

```C++
'''
Date 12-10-2021

In this tutorial, you will learn about Multilevel Inheritance
'''


class Grand_Father:
    name = "None"

    def __init__(self, name):
        self.name = name


class Dad(Grand_Father):
    basket_ball = 1

    def basket_ball_very_base_class(self):
        print(
            f"My name is {self.name} and I play Basket ball {self.basket_ball} times a day.")


class Son(Dad):
    dance = 2

    def dance_base_class(self):
        print(
            f"My name is {self.name} and I do dancing {self.dance} times a day.")


class Grand_Son(Son):
    play = 2

    def play_derived_class(self):
        print(f"My name is {self.name} and I play {self.play} times a day.")


rohit = Grand_Son("Rohit")
rohit.play_derived_class()
# print(rohit.basket_ball)

```

---

---

## **_12.) tutorial_62_2_exercise of Python_**

### [**_Click me_**](tutorial_62_2_exercise.py "Clike here to see full file") to see full file of tutorial_62_2_exercise

```C++
'''
Date 12-10-2021

This tutorial is an exercise in which you need to make a new group of classes which uses DRY principal and shows the multilevel inheritance in them.
You can use Electronic devices to demonstrate this.

Electronic_Devices
        ^
        |
    Telephones
        ^
        |
   Mobile_Phones
        ^
        |
    Smart_Phones

'''


class Electronic_Devices:
    voltage_rating = 0
    name = "None"

    def __init__(self, name="Not Defined", voltage_rating=0):
        self.name = name
        self.voltage_rating = voltage_rating


class Telephones(Electronic_Devices):
    frequency = 0

    def __init__(self, name="Not Defined", voltage_rating=0, frequency=0):
        super().__init__(name, voltage_rating)
        self.frequency = frequency

    def print_info(self):
        print(
            f"Name of the device is {self.name}\nVoltage Rating of the device is {self.voltage_rating} volt\nFrequency of the device is {self.frequency} Hz")


class Mobile_Phones(Telephones):
    weight = 1000

    def __init__(self, name="Not Defined", voltage_rating=0, frequency=0, weight=1000):
        super().__init__(name, voltage_rating, frequency)
        self.weight = weight

    def print_info(self):
        super().print_info()
        print(
            f"Weight of the device is {self.weight} gram")


class Smart_Phones(Mobile_Phones):
    thickness = 1000
    warranty = 0
    internet_max_speed = 0

    def __init__(self, name="Not Defined", voltage_rating=0, frequency=0, weight=1000, thickness=1000, warranty=0, internet_max_speed=0):
        super().__init__(name, voltage_rating, frequency, weight)
        self.thickness = thickness
        self.warranty = warranty
        self.internet_max_speed = internet_max_speed

    def print_info(self):
        super().print_info()
        print(
            f"Thickness of the device is {self.thickness} mm\nWarranty of the device is {self.warranty} year\nInternet\'s maximum speed of the device is {self.internet_max_speed} Kb/s\n")


phone = Smart_Phones("Nokia 0154", 4.9, 2.6, 94.5, 12.4, 2.5, 6)
phone.print_info()

```

---

---

## **_13.) tutorial_63 of Python_**

### [**_Click me_**](tutorial_63.py "Clike here to see full file") to see full file of tutorial_63

```C++
'''
Date 12-10-2021

In this tutorial, you will learn about Public, Protected, and Private Access Modifiers
Unlike C++ which allows us to make Public, Protected, and Private variable Syntactically
Python does not provide any special facility for making diffrent types of Access Modifiers
So we use the following conventions---
For Public    === var
For Protected === _var
For Private   === __var
'''


class A:
    var = "I\'m a Public variable of class A"
    _var = "I\'m a Protected variable of class A"
    __var = "I\'m a Private variable of class A"


val = A()

print(val.var)
print(val._var)
# * The below line will throw an error because Python had done name mangling on __var
# ? print(val.__var)
# * The above line will throw an error because Python had done name mangling on __var

# * The below line will will not give an error
print(val._A__var)
# * The above line will will not give an error

```

---

---

## **_14.) tutorial_65 of Python_**

### [**_Click me_**](tutorial_65.py "Clike here to see full file") to see full file of tutorial_65

```C++
'''
Date 12-10-2021

In this tutorial, you will learn about Super() and about overtiding in classes
'''


class A:
    var_of_A = 1

    def print_info(self, var_of_A):
        self.var_of_A = var_of_A
        print("I\'m in class A, var_of_A =", self.var_of_A)


class B(A):
    var_of_B = 2

    def print_info(self, var_of_B=2, var_of_A=1):
        self.var_of_B = var_of_B
        super().print_info(var_of_A)
        print("I\'m in class B, var_of_B =",  self.var_of_B)


class C(B, A):
    var_of_C = 3

    def print_info(self, var_of_C, var_of_A=1, var_of_B=2):
        self.var_of_C = var_of_C
        super(C,  self).print_info(var_of_B, var_of_A)
        print("I\'m in class C, var_of_C =", self.var_of_C)


obj = C()
obj.print_info(var_of_C=45,
               var_of_A=34,
               var_of_B=988)

```

---

---

## **_15.) tutorial_66 of Python_**

### [**_Click me_**](tutorial_66.py "Clike here to see full file") to see full file of tutorial_66

```C++
'''
Date 12-10-2021

In this tutorial, you will learn about Diamond Shape Problem

        A
        ^
       / \
      B   C
      ^   ^
      \   /
        D
'''


class A:
    @staticmethod
    def met():
        print("I\'m in Class A")


class B(A):
    @staticmethod
    def met():
        print("I\'m in Class B")


class C(A):
    @staticmethod
    def met():
        print("I\'m in Class C")


class D(B, C):
    pass
    # @staticmethod
    # def met():
    #     print("I\'m in Class D")


obj = D()
obj.met()

```

---

---

## **_16.) tutorial_67 of Python_**

### [**_Click me_**](tutorial_67.py "Clike here to see full file") to see full file of tutorial_67

```C++
'''
Date 12-10-2021

In this tutorial, you will learn about Dunder Methods
You can see the python documentation for more information of diffrent types of dunder methods
and to get to the documentation just search "mapping operators to function in python"
'''


class Employee:
    number_of_leaves = 15
    name = "Unknown"
    salary = 100

    def __init__(self,  name, salary, number_of_leaves):
        self.number_of_leaves = int(number_of_leaves)
        self.name = name
        self.salary = int(salary)

    def print_details(self):
        print(
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}")

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave

    @classmethod
    def alternative_constructor_for_class(cls, str, split_symbol='-'):
        return cls(*str.split(split_symbol))

    def __add__(self, other):
        return f"Sum of {self.name}\'s and {other.name}\'s salary is {self.salary + other.salary}"

    def __matmul__(self, other):
        return f"2 * sum of {self.name}\'s and {other.name}\'s salary is {(self.salary + other.salary)*2}"

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}"

    def __repr__(self):
        return f"Employee(\"{self.name}\", {self.salary}, {self.number_of_leaves})"


aman = Employee("Aman", 100, 11)
rohan = Employee.alternative_constructor_for_class("Rohan-200-54")

# print(aman+rohan)
# print(aman @ rohan)
print(rohan, "\n\n")
print(repr(rohan))

```

---

---

## **_17.) tutorial_68 of Python_**

### [**_Click me_**](tutorial_68.py "Clike here to see full file") to see full file of tutorial_68

```C++
'''
Date 12-10-2021

In this tutorial, you will learn about Abstract base Class
Note: If you use Abstract base Class with function declared with method "@abstractmethod" then that function must be declared in further derived class
'''

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0


class Rectangle(Shape):
    height = 0
    width = 0

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def print_area(self):
        print(
            f"Are of rectangle with width {self.width}cm and height {self.height}cm is {self.height*self.width}")


rect = Rectangle(8, 9)
rect.print_area()

```

---

---

## **_18.) tutorial_69_1 of Python_**

### [**_Click me_**](tutorial_69_1.py "Clike here to see full file") to see full file of tutorial_69_1

```C++
'''
Date 12-10-2021

In this tutorial, you will learn about Setters, and property Decorators
'''


class Employee:
    number_of_leaves = 15
    name = "Unknown"
    salary = 100

    def __init__(self,  name, salary, number_of_leaves):
        self.number_of_leaves = int(number_of_leaves)
        self.name = name
        self.salary = int(salary)

    def print_details(self):
        print(
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}\nEmail is {self.return_email}")

    @property
    def return_email(self, mail="gmail"):
        return f"{self.name}@{mail}.com"

    @return_email.setter
    def return_email(self, email_address="None@gmail.com"):
        if '@' not in email_address:
            raise ValueError("Not a valid email address")
        try:
            self.name = email_address.split('@')[0]
        except print(0):
            print("Error while setting name")

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave

    @classmethod
    def alternative_constructor_for_class(cls, str, split_symbol='-'):
        return cls(*str.split(split_symbol))

    def __add__(self, other):
        return f"Sum of {self.name}\'s and {other.name}\'s salary is {self.salary + other.salary}"

    def __matmul__(self, other):
        return f"2 * sum of {self.name}\'s and {other.name}\'s salary is {(self.salary + other.salary)*2}"

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}"

    def __repr__(self):
        return f"Employee(\"{self.name}\", {self.salary}, {self.number_of_leaves})"


aman = Employee("Aman", 4000, 14)
# aman.print_details()
print(aman.return_email)
aman.return_email = "Aman0864@gmail.com"
print(aman.return_email, "\n")
aman.print_details()
# print(aman._Employee__return_email())

```

---

---

## **_19.) tutorial_69_2 of Python_**

### [**_Click me_**](tutorial_69_2.py "Clike here to see full file") to see full file of tutorial_69_2

```C++
'''
Date 12-10-2021

In this tutorial, you will learn about Setters, Deleter, and property Decorators
'''


class Employee:
    number_of_leaves = 15
    name = "Unknown"
    salary = 100

    def __init__(self,  name, salary, number_of_leaves):
        self.number_of_leaves = int(number_of_leaves)
        self.name = name
        self.salary = int(salary)

    def print_details(self):
        print(
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}\nEmail is {self.return_email}")

    @property
    def return_email(self, mail="gmail"):
        if self.name == None:
            return "Email is not defined (You can set it using Setter)"
        return f"{self.name}@{mail}.com"

    @return_email.setter
    def return_email(self, email_address="None@gmail.com"):
        if '@' not in email_address:
            raise ValueError("Not a valid email address")
        try:
            self.name = email_address.split('@')[0]
        except print(0):
            print("Error while setting name")

    @return_email.deleter
    def return_email(self):
        self.name = None

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave

    @classmethod
    def alternative_constructor_for_class(cls, str, split_symbol='-'):
        return cls(*str.split(split_symbol))

    def __add__(self, other):
        return f"Sum of {self.name}\'s and {other.name}\'s salary is {self.salary + other.salary}"

    def __matmul__(self, other):
        return f"2 * sum of {self.name}\'s and {other.name}\'s salary is {(self.salary + other.salary)*2}"

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}"

    def __repr__(self):
        return f"Employee(\"{self.name}\", {self.salary}, {self.number_of_leaves})"


aman = Employee("Aman", 4000, 14)
print(aman.return_email)
del aman.return_email
print(aman.return_email)

aman.print_details()

```

---

---

## **_20.) tutorial_70_1 of Python_**

### [**_Click me_**](tutorial_70_1.py "Clike here to see full file") to see full file of tutorial_70_1

```C++
'''
Date 12-10-2021

In this tutorial, you will learn about Object Introspection
Note: Object Introspection is used to know all the information about a particular object
'''


class Employee:
    number_of_leaves = 15
    name = "Unknown"
    salary = 100

    def __init__(self,  name, salary, number_of_leaves):
        self.number_of_leaves = int(number_of_leaves)
        self.name = name
        self.salary = int(salary)

    def print_details(self):
        print(
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}\nEmail is {self.return_email}")

    @property
    def return_email(self, mail="gmail"):
        if self.name == None:
            return "Email is not defined (You can set it using Setter)"
        return f"{self.name}@{mail}.com"

    @return_email.setter
    def return_email(self, email_address="None@gmail.com"):
        if '@' not in email_address:
            raise ValueError("Not a valid email address")
        try:
            self.name = email_address.split('@')[0]
        except print(0):
            print("Error while setting name")

    @return_email.deleter
    def return_email(self):
        self.name = None

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave

    @classmethod
    def alternative_constructor_for_class(cls, str, split_symbol='-'):
        return cls(*str.split(split_symbol))

    def __add__(self, other):
        return f"Sum of {self.name}\'s and {other.name}\'s salary is {self.salary + other.salary}"

    def __matmul__(self, other):
        return f"2 * sum of {self.name}\'s and {other.name}\'s salary is {(self.salary + other.salary)*2}"

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}"

    def __repr__(self):
        return f"Employee(\"{self.name}\", {self.salary}, {self.number_of_leaves})"


aman = Employee("Aman", 4000, 14)

print(type(aman.name))
print(type(aman))
print(id(aman.name))
print(id(aman))
# print(dir(aman.name))
print(dir(aman))

```

---

---

## **_21.) tutorial_70_2 of Python_**

### [**_Click me_**](tutorial_70_2.py "Clike here to see full file") to see full file of tutorial_70_2

```C++
'''
Date 12-10-2021

In this tutorial, you will learn about Object Introspection
Note: Object Introspection is used to know all the information about a particular object
'''

import inspect


class Employee:
    number_of_leaves = 15
    name = "Unknown"
    salary = 100

    def __init__(self,  name, salary, number_of_leaves):
        self.number_of_leaves = int(number_of_leaves)
        self.name = name
        self.salary = int(salary)

    def print_details(self):
        print(
            f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}\nEmail is {self.return_email}")

    @property
    def return_email(self, mail="gmail"):
        if self.name == None:
            return "Email is not defined (You can set it using Setter)"
        return f"{self.name}@{mail}.com"

    @return_email.setter
    def return_email(self, email_address="None@gmail.com"):
        if '@' not in email_address:
            raise ValueError("Not a valid email address")
        try:
            self.name = email_address.split('@')[0]
        except print(0):
            print("Error while setting name")

    @return_email.deleter
    def return_email(self):
        self.name = None

    @classmethod
    def change_leaves(cls, leave=10):
        cls.number_of_leaves = leave

    @classmethod
    def alternative_constructor_for_class(cls, str, split_symbol='-'):
        return cls(*str.split(split_symbol))

    def __add__(self, other):
        return f"Sum of {self.name}\'s and {other.name}\'s salary is {self.salary + other.salary}"

    def __matmul__(self, other):
        return f"2 * sum of {self.name}\'s and {other.name}\'s salary is {(self.salary + other.salary)*2}"

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}\nNumber of leaves left are {self.number_of_leaves}"

    def __repr__(self):
        return f"Employee(\"{self.name}\", {self.salary}, {self.number_of_leaves})"


aman = Employee("Aman", 4000, 14)

for i in inspect.getmembers(aman):
    print(i)

```

---

---
