from abc import ABCMeta, abstractmethod
from types import ClassMethodDescriptorType

class Employee(metaclass = ABCMeta):
    typee = 6
    no_of_pages = 98

    @abstractmethod
    def print_met(self):
        print("I'm an Abstract Method")

    def __init__(self, name, role):
        self.name = name
        self.role = role
                                # Always, Remember that Abstract Base Class can't make Any Object, otherwise it will retrun Error
                    
try:
    at = Employee('dfdkfj', 'dfkdjf')
except TypeError as TeryERR:
    print(TeryERR)

class Clark(Employee):
    typee = 69
    descirp = 'We are Clarks....!!!'
    
    @classmethod
    def cls_change(cls, string):
        params = string.split('-')

        return cls(*params)
    
    @classmethod
    def chane_cls_attribute(cls, typee, description):
        cls.typee = typee
        cls.descirp = description

    def print_met(self):
        print("I'm an Abstract Method")


emp1 = Clark('Smasher', 'Arasaka')
print(emp1.print_met())
print(emp1.no_of_pages)

cmp = Clark.cls_change('Jhonny-Devlop')          # using ClassMethod as an Alternative of Constructor, 
print(cmp.name)

emppdf = Clark.cls_change('Judy-Cleaner')

# print(emppdf.name)
# print(emppdf.role)



# class Another(Clark, Employee):
#     all_roundes = 'All Rounder'
#     __private_attribute = 'Private'
#     _protected = 'Protected'

#     @staticmethod
#     def khamaka_printer_met():
#         print('Hey, we are alrounder')

#     # def p'rint_met(self):
#     #     print("Im an Abstract Method")

# other_emp = Another.cls_change('Other-Emolpyee')
# other_emp.khamaka_printer_met()
# print(other_emp.name)

# other_emp = Another('Hello', 'Howdy')
# print(other_emp.name)
# print(other_emp.role)
# emp1.chane_cls_attribute(665, 56465)
# print(Clark.no_of_pages, Clark.typee)
# print(Another._protected)
# print(other_emp._protected)
# try:
#     print(Another.__private_attribute)
# except AttributeError as atterER:
#     print(Another._Another__private_attribute)
#     print(other_emp._Another__private_attribute)



