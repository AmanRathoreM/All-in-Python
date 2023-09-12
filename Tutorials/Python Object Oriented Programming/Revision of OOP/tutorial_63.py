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
