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
