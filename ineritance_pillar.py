# base class have no accsees of son class but son have access of all the fnction of Father

# Single Inheritance  :one base class and one derived class
#
# class Father:                               # Base class
#     def __init__(self,a):
#         self.name="Father"
#         self.a=a
#         print("father constructor")
#
#     def   teacher_maths(self):                   #method
#         school_name = "EVM"
#         return  school_name
#
#
# class Son(Father):                          # Derive class
#
#     def __init__(self):
#         super().__init__()
#         self.name = "Son"
#
#     def teacher_python(self):
#         Institute_name = "TechAmplifiers" * self.a
#         return  Institute_name
#
#
#
# # f = Father(1)
# # f.teacher_maths()        #output :none
# # print(f.name)
#
# s = Son()
# # print(s.name)
# # s.teacher_python()        #output :none
# # s.teacher_maths()
# # print(s.teacher_maths()) # it will print because we take return value  othwerwise it will empty
#
# print(s.teacher_python()) # also this

# exaple of only one constructor in program or without constructor in son  class


# class Father:  # Base class
#     def __init__(self, a):
#         self.name = "Father"
#         self.a = a
#         self.b=10
#         print("father constructor")
#
#     def teacher_maths(self):  # method
#         school_name = "EVM"
#         return school_name
#
#
# class Son(Father):  # Derive class
#      def teacher_python(self):
#         Institute_name = "TechAmplifiers" * self.a
#         return Institute_name
#
#
# s = Son(10)           # must to pass value of havinG father constructor  because only one constructor is there
# print(s.name)
# s.a= 20         # we also modify valuse using son object  of father values
# print(s.a)
# s.teacher_python()  # output :none
# s.teacher_maths()


# multiple Inheritance  : multiple base class(mother father and also grand father and grand mother) and one derived class

# class Mother:                               # Base class1
#     def __init__(self):
#         self.name="Father"
#
#     def   teacher_maths(self):              # method
#         school_name = "EVM"
#         return  school_name
#

# class Father:                               # Base class2
#     def __init__(self):
#         self.name="Father"
#
#     def   teacher_maths(self):              #  method
#         school_name = "EVM"
#         return  school_name
#
#
# class Son(Father,Mother):   # Derive class having accsess of both Father,Mother
#
#     def __init__(self):
#         self.name = "Son"
#
#     def teacher_python(self):
#         Institute_name = "TechAmplifiers"
#         return  Institute_name
#


# example Practice

# class Father:  # Base class
#
#     def __init__(self):
#         self.name = "Father"
#         self.a = 10
#         print("father constructor")
#
#     def teacher_maths(self):  # method
#         school_name = 2 * self.a
#         return school_name
#
#
# class Son(Father):  # Derive class
#
#     def __init__(self):
#         # here we print supeer function out put is differnt
#         self.name = "Son"
#         print("son constructor")
#         super().__init__()  # print here  super function output different
#
#     def teacher_python(self):
#         Institute_name = 15 * self.a
#         return Institute_name
#
#
# s = Son()

print(s.teacher_python())


# Multilevel Inheritance

# there having base class and first level inheritance(der1) and second level inheritance(der2)

# class GrandFather:             #            base
#     def __init__(self):
#         self.name="Father"
#
#     def  farmer(self):
#         school_name = "EVM"
#         return  school_name
#
#
# class Father(GrandFather):           # first generation or level Inheritance
#     def __init__(self):
#         self.name="Father"
#
#     def   teacher_maths(self):
#         school_name = "EVM"
#         return  school_name
#
#
# class Son(Father):                   # Second generation or level Inheritance
#
#     def __init__(self):
#         super().__init__()
#         self.name = "Son"
#
#     def teacher_python(self):
#         Institute_name = "TechAmplifiers"
#         return  Institute_name
#
#
#
#
# s=Son()       # have accses of both methods farmer as well as  maths teacher
# s.
# f=Father()
# f.             # have accses of farmer


# heirarchical Inheritance


# one base class and  multiple Derived class
class Father:
    def __init__(self):
        self.name = "Father"

    def teacher_maths(self):
        school_name = "EVM"
        return school_name


class Son(Father):

    def __init__(self):
        super().__init__()
        self.name = "Son"

    def teacher_python(self):
        Institute_name = "TechAmplifiers"
        return Institute_name


class Daughter(Father):

    def __init__(self):
        super().__init__()
        self.name = "Son"

    def doctor(self):
        Hospital = "teeth spescialist"

# Daughter and son can have accsess of Father but no accsess to each other like son to daughter and Daughter to son


# hybrid Inheritance


# there is an combination of multiple inheritance
