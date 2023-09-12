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
