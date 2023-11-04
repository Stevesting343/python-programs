# how to write a program

# object is an instance of class
# class c is small
# class name start with capital letter
# class is blueprint(structure) of an object
# object strored at different different memeory location


# reformat code  on program right click on the

# def python1():  # bracket it is "function"
#     a = 10


# python1()

# -------------------    we have add two blank spaces between function and class and between class properway of writing
#
# class Python:  #class name should in capital letter or first word is capital
#     a = 10
#     b = 20
#     c = 30
#
#  # all the created object work as different we change one object it can't affect another object
#
# obj = Python()
# print(obj.a)
#
# hiibro = Python()
# print(obj.b)
#
# a =Python()
# print(a)
#
# obj.a = 50
# print(Python().a) # we can't print modified value without obj beacuse the access is to the 'obj' see below example
#           # it will call in the class variable not modified variable value
#
# obj.a = 50
# print(obj.a)
#
# a =Python()
# print(a)
#
# Python().a=50  # it is not run properly
#  print(Python().a)            # using (.)operator we accsees attributes or variable

#rules
# In 'class' function is not function it will call 'Method'
# to access same variable in all methods in class can access with the self keyword
# def __init__(self): this is constructor(construcor is also a function)
# types of constructor default and parameterized constructor
#we not take multiple constructor in same class
# variable names and function or method names  should not same it will shows an error


# example of Default constructor
# default constructor we not pass value at object call
# class Python:
#     def __init__(self): # constructor is use to initialize(assign values) to data memeber of class when class obj created
#         self.x = 29
#         self.y = 31
#         self.z = 100
#         print("i am constructor",self.x)
#
#     def oops(self):
#         print(self.x)
#         self.n = 25
#         return 0
#
#     def fun(self):
#         print(self.y)
#         self.a = 50  # but not declare in the next function
#         print(self.n)
#         return 0
#
#     def course(self):
#         print(self.z)
#         print(self.a)  # we accsess variable inside one method to another
#
#
# obj = Python()  # it will not take values to the values to default constructor
# obj.oops()  # object for methods or function
# obj.fun()
# obj.course()
# obj.x = 20
# print(obj.x)


#  example of parameterized constructor

# class Python:
#     def __init__(self, x, y, z):
#         self.x = x  # x hya parameter chi value assign zali self.x hya instance la we call it as instance of variable
#         self.y = y
#         self.z = z
#         print("i am constructor",self.x)
#
#     def oops(self):
#         print(self.x)
#         self.n = 25
#         return 0
#
#     def fun(self):
#         print(self.y)
#         self.a = 50  # but not declare in the next function
#         print(self.n)
#         return 0
#
#     def course(self):
#         print(self.z)
#         print(self.a)  # we accsess variable inside one method to another



# obj = Python(10, 20, 30)  # we give the values to parameterized constructor
# obj.oops()  # object for methods or function
# obj.fun()
# obj.course()
#
# obj.x = 20
# print(obj.x)

#-------------------------------------------

# class Python:
#     def __init__(self,x,y,z):
#         self.a = x          # we dont write like    self.x = a
#         self.a = 25
#         self.b = y          # we dont write like    self.y = b
#         self.c = z          # we dont write like    self.z = c
#         print("This is Constructor")
#
# m = Python(1,2,3)
# print(m.b)
#
# d = Python(2,1,3)
# print(d.a)        # ha updated value ghetoy


#-------------------------------

# class Dheeraj:
#     x = 20    # this is class variable
#     def __init__(self):
#         self.a = 1
#         print('hello i  am constructor')
#
# m = Dheeraj()
# print(m.x)  #print kela class variable
# print(m.a)


#------------------------------------------------

# class Info:
#
#       def __init__(self,name,age,collage):
#             self.n = name
#             self.a = age
#             self.c = collage
#             print("hii consructor here")
#
#       def names(self):
#           print("This is names function/method")
#           print(self.n)
#
#       def ages(self,v):
#           print(self.a)
#
#       def collages(self):
#           print(self.c)
#           return self.a   # when print method at time of object call then and then only the return value goes to function and print()
#
#
# o = Info("Dheeraj",19,'Kaveri(khs)')
# # print(o.n)         # variable calling
# # print(o.a)
# # print(o.c)
#
# o.names()     # method calling
# o.ages(2)     # it will not take value inside method ages paramter at method call
# print(o.ages) first it call function colages inside self.c and then return value


# these are two combine classes personal Deatils And Educational details
#
# class PersonalDetails:        # we don't write class name like "Personal_Details"
#
#       def __init__(self,name,age,dob,address,mob,email):
#             self.n=name
#             self.a=age
#             self.date=dob
#             self.addr=address
#             self.mob=mob
#             self.email=email
#
#       def names(self):
#           print(self.n)
#
#       def ages(self):
#           print(self.a)
#
#       def dobs(self):
#           print(self.date)
#
#       def addrs(self):
#           print(self.addr)
#
#       def mobno(self):
#           print(self.mob)
#
#       def emails(self):
#           print(self.email)
#           return "this is dheeraj"
#
#
# class EducationDeatils:
#     def __init__(self,tenth,twelve,graduation):
#         self.tenth = tenth
#         self.twelve = twelve
#         self.graduation = graduation
#
#         print("I am constructor Dheeraj sir")
#     def ten(self):
#         print(f'this is my tenth marks {self.tenth} ')
#
#     def twe(self):
#         print(f'this is my twelve marks {self.twelve} ')
#
#     def g(self):
#         print(f'this is my Graduation marks {self.graduation} ')
#
# obj = PersonalDetails("dheeraj", 18, '15/05/2001', "Mh", 9093323948, "Dhirajkadu@gmail.com")
# obj.names()
# obj.ages()
# obj.dobs()
# obj.addrs()
# obj.mobno()
# obj.emails()
# print(obj.emails())  # print return value using this syntax
#
# print(obj.n)
#         # print for variable
#
# hey = EducationDeatils(90,70,90)
#
# hey.ten()
# hey.twe()
# hey.g()


































































































