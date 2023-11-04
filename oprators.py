#
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high")
# print("\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t	How I wonder what you are!")
#


# import datetime
# now = datetime.datetime.now()
# print("Current date and time : ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# def calculate():
#     print("hii")
#     return "helloe"
#
# calculate()


# def area_of_circle(r):
#
#     A = 3.14 * r * r
#     print("Area of circle", A)
#     return "h"
#
# area_of_circle(6)
#


# def reversed(s):
#     str = ""
#     for i in s:
#         str =  i + str  # here we take i + str thats why it can add the name in reverse order "skeegrofskeeG"
#     return str          # we do like str = str + i  print like output:"Geeksforgeeks"
#
#
# s = "Geeksforgeeks"
# print("The reversed string(using loops) is : ")
# print(reversed(s))


# def reversed(f):
#    full_name = " "
#
#    for i in f:
#        full_name = i + full_name
#    return full_name
#
#
#
# f = "Dheeraj Kadu"
# reversed(f)
# print(reversed(f))

# convert string input 3,5,7,23 seprated by comma convet them in to string
# s = "3", "5", "7", "23"
# print(list(s))
# print(tuple(s))
#


# a = input()     # split method use to conert string into list
# b = a.split(",") # split method  use with string only then the
# print(b)          #no. entered as string that have convert into string

# values = input("Input some comma seprated numbers : ")
# list1 = values.split(",")
# print(list1)


# 7. Write a Python program that accepts a filename from the user and prints the extension of the file

# input: abc.java

# filename = input()
#
# print(filename,".java")

# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print(f_extns)
# print ("The extension of the file is : " + repr(f_extns[-1]))

#
# color_list = ["Red","Green","White" ,"Black"]
#
# r = color_list[0]
#
#
# for i in color_list:
#   print(".")
# print(i)
#
#

'''9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''

# date and time
'''
exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i" % exam_st_date)
 # with help of % sign it gives accsess to the %i

from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

'''

# n = int(input())
# for i in range(2, n+1):
#     count = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#            count += 1
#     if count == 2:
#         print(i)
#
# l = [22, 38, 19, 65, 57, 39, 152, 621, 161, 44, 90, 190]
# print(list(filter(lambda n : (n % 19) == 0, l)))
# print(list(filter(lambda a : (a % 23) == 0, l)
# t = 3
# d ={ ("sam", 99912222), ("tom", 11122222), ("harry", 12299933)}
# # print(dict(d))
# print(dict(map(lambda n:nif print(n) else print("not found"), d)))

# update or add the key value in dictionary

# d = {
#     'key1': "dheeraj",
#     'key2': "raj"
# }
#
# d.update({'key3': 'yellow'})
# print(d)

# add dictionary in sequence

dic1 = {1: 10, 2: 20}

dic2 = {3: 30, 4: 40}

dic3 = {5: 50, 6: 60}


# for i in dic1, dic2, dic3:
#
#     di4 += i
#
# print(di4)


# add dictionary using merge operator ' | '
#
# dict1 = {'a': 'one', 'b': 'two'}
#
# dict2 = {'b': 'letter two', 'c': 'letter three'}
#
# dict3 = dict1 | dict2    # what is the name of the operator use here
#
# print("dict3: ", dict3)

# di = ''
# for d in (dic1, dic2, dic3):
#
#     di += d

#
# list1 = [1, 2, 4]
#
# suma = 0
#
# for i in list1:
#     suma += i
#
# print(suma)

# take list from user

#
# li = []
# n = int(input("enter no of list elements we want to add :"))
# for i in range(1, n+1):
#
#     ele = int(input())
#     li += str(ele)
#
# print(li)


# sum of list
# list2 = [1, 2, 3, -8]
# suma = 0
# for i in list2:
#     suma += i
#
#
# print(suma)

# multiply the list element

# list2 = [1, 2, 3, 4]
# mult = 1
#
# for i in list2:
#     mult *= i
#     print(mult)
#
# print()

# max num in list
# def max_num_in_list(list):
#     max = list[0]
#     for a in list:
#         if a > max:
#             max = a
#     return max
#
#
# print(max_num_in_list([1, 2, 5, 4, 1]))


# min num in list
# def smallest_num_in_list(list):
#     min = list[1]
#     for a in list:
#         if a < min:
#             min = a
#     return min
#
#
# print(smallest_num_in_list([1, 2, 4, 5]))



