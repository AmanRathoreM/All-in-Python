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
