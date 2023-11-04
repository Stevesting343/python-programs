
# from abc import ABC, abstractmethod
#
#
# class Father(ABC):  # Abstract Base Class
#     def __init__(self):
#         print('father constructor')
#
#     @abstractmethod
#     def teaching(self):  # abstract method
#         # we no need to write the working (it is empty.. it will override in subclass)
#         pass  # it keyword it perform null operation
#
#     def teaching_maths(self):
#         print("Teaching maths...")
#
#
# class Son(Father):  # Abstract class
#     def __init__(self):
#         super().__init__()
#         print('son constructor')
#
#     @abstractmethod
#     def teaching(self):
#         pass
#
#
# class Dheeraj(Son):  # Abstract class
#     def __init__(self):
#         super().__init__()
#         print('son constructor')
#
#     def teaching(self):  # actual implementaion is here of abstarct method
#         print("Teaching Python")
#
# try:
#     f=Father()
#     f.teaching()
#     s= Son()
#     s.teaching()
#     s.teaching_maths()
#     # # d = Dheeraj() uncomment this and run but below that all commented
# except:
#       print("can't create object of SON and father class because abstract method is used ")
#
# else:
#
#     d = Dheeraj()
#     d.teaching()
#
# finally:
#     print("Working")


# divide by zero      example

# raise E          #type raise and Exception E
# a = 10
# count=0
# try:
#     for i in range(0,10):
#         if i == 3:
#             raise ZeroDivisionError("i cannot be 3")
#         elif i == 2:
#             raise ValueError("This is value error and i cannot be neagtive or zero")
#         print(a/(i-3))
#         count += 1
# except ZeroDivisionError as z:
#     print("error", z)
# except ValueError as ve:
#     print("error", ve)
# else:
#     print(count)
# finally:
#     print(count)
#     print(a)


S = input()

try:
   if S.isdigit():
      int_input = int(S)
      print(int_input)

   else:

       raise ValueError("Bad String")

except ValueError as ve:
    print(ve)

# else:
#     print("hello")
# finally:
#     print("Working")
