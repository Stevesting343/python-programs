# lambda function

# a = lambda a, b, c, d: a+b+c+d  # can have only one expression but multiple arguments
# #print(a)           # it will shows function lambda and memeory location
# print(a(1, 2, 3,4)) # we must pass all the values
# n = a(1, 2, 3, 4)     # or like this
# print(n)

# we assign function to a variable like 'a'
# it also known as one linar code and also Higher order functions

# multiplication
# s = lambda a,b:a*b
# print(s(10,20))

# ----------
#
# def fun(n):
#
#     return 2 * n
#
# print(fun(2))

# --------------------

#
#
# def fun(n):
#
#     return lambda a: a * n
#
# double = fun(2)   # this will assign value to " n "
# triple = fun(3) # it assign all the lambda function (lambda a: a * 3) to triple variable
# four = fun(4)   #lambda a: a * 4
# print(double(11)) # this will assign value to " a "
# print(triple(22))
# print(four(5))

# a=fun(2) #it will nothing without this
# print(fun(5)(4))

# #--------------------------
#
# num= lambda a:a/17==0
#
# #num(34)    #not get ouput from the line of code
# print(num(34))
#
# #------------
# num= lambda a:a%17==0
#
# #num(34)    #not get ouput from the line of code
# print(num(34))
#
#  #output true or false
#  #-------------------
# num= lambda a:a/17
#
# #num(34)    #not get ouput from the line of code
# print(num(34))
#
# -------------------
# we can write lambda function within function = no

# # example
# def divide(n):
#     return lambda a: a % n == 0
#
#
# no_divisible_by17 = divide(17)
# no_divisible_by7 = divide(7)
#
# print(no_divisible_by17(51))
# print(no_divisible_by7(49))
# print(no_divisible_by7(4))



# example of assignments  no. is divisible by 19 or 23

l = [22, 38, 19, 65, 57, 39, 152, 621, 161, 44, 90, 190]
l2= []

count=0
for i in l:
    if i % 19 == 0:
        print(i)
    else:
       l2.append(i)
print(l2)






