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
