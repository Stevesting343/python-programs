# polymorphism (many form )          example :me dheeraj my many forms like (i am son ,student,friend etc)

# method Overloading

# same name different paramters
# python having 'bottom up' approach
# the method can not be achieved
# in one class we dont write same method


# class Person:
#     def __init__(self):
#         print("I am a constructor")
#
#     def add(self,a,b):
#         return
#     def add(self,a,b,c):
#         return a+b+c
#
# p=Person()
# print(p.add(10,20))
# print(p.add(10,20,30))


# jugad ahai varchya method achive karaycha pan add method 2 vela nahi use karun shakat
# but this can be achieved whwn oeration same asel like +,-,* etc

# class Person:
#     def __init__(self):
#         print("I am a constructor")
#
#     # def add(self, a, b):      # but we dont write this method again method overloading is differnt
#     #     return
#
#     def add(self, a, b, c=0): # we want to pass default argument
#         return a + b + c
#
#
# p = Person()
# print(p.add(10, 20))
# print(p.add(10, 20, 30))


# Method overriding

# same name & same Parameter
# it occurs within inheritance or need of Inheritance

class Father:
    def __init__(self):
        print('father constructor')

    def  teaching(self):
        print("Teaching...")

    def teaching_maths(self):
            print("Teaching maths...")

class Son(Father):
    def __init__(self):
        super().__init__()
        print('son constructor')

    def teaching(self):
        print("Teaching Python")


s = Son()
s.teaching()      #the base class teaching method get override or hidden  derived teaching method
s.teaching_maths()






















