# Abstraction
# Python does not provide  abstract  classes
# module is single file  having clases like ABC  helper class
# which class perform contains abstract method we can not create object of the that class beacause the class method
# is in underconstruction we cannot instantiated the object of that class
# but instantiate the class or subclass having actual  implematation of that method
# we can create multiple abstract class but not instantiated the object of that class
# need of inheritance
# abc.py is a module


# from abc import ABC,abstractmethod
#
#
# class Father(ABC):      # Abstract Base Class
#     def __init__(self):
#         print('father constructor')
#
#     @abstractmethod
#     def  teaching(self): # abstract method
#                       # we no need to write the working (it is empty.. it will override in subclass)
#        pass          # it keyword it perform null operation
#
#     def teaching_maths(self):
#             print("Teaching maths...")
#
# class Son(Father):      # Abstract class
#     def __init__(self):
#         super().__init__()
#         print('son constructor')
#     @abstractmethod
#     def teaching(self):
#        pass
#
# class Dheeraj(Son):      # Abstract class
#     def __init__(self):
#         super().__init__()
#         print('son constructor')
#
#     def teaching(self):           # actual implementaion is here of abstarct method
#         print("Teaching Python")
#
# d= Dheeraj()
# d.teaching()

# Accsess specifier
# class Company:
#     def __init__(self):
#         print("constructor")
#
#     def reception(self):
#         print("recption")
#
#     def _sales(self):
#          print("sales")
#
#     def __account(self):
#         print("account")
#
#
# c= Company()
# c.reception()
# c._sales()        # we want to ask then it will call
# c.__account()     #it dont have accsess from any way


# exapmple of abstraction

# you have to implement  abstraction in  school
# Abstract base class - principle
# abstract class - HOD
# classes teachers -- methods need to abstract teaching_maths,science ,art

from abc import ABC, abstractmethod


class Principle(ABC):
    def __init__(self):
        self.a = 10
        print("This Principle constructor")

    @abstractmethod
    def teaching_marathi(self):
        pass

    @abstractmethod
    def teaching_english(self):
        pass


class HOD(Principle):

    def __init__(self):
        super().__init__()
        self.b = 20
        print("This HOD constructor")

    @abstractmethod
    def teaching_maths(self):
        pass

    @abstractmethod
    def teaching_science(self):
        pass


class Teachers(HOD):

    def __init__(self):
        super().__init__()

        self.c = 30
        print("This Teachers constructor")

    def teaching_maths(self):
        return "I am teaching maths"

    def teaching_science(self):
        return "I am teaching science"

    def teaching_marathi(self):
        return "I am teaching marathi"

    def teaching_english(self):
        return "I am teaching marathi"


t = Teachers()
t.teaching_english()
t.teaching_maths()
t.teaching_marathi()
t.teaching_science()
