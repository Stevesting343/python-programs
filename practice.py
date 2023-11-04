'''i = 4
d = 4.0
s = 'HackerRank '
i1= 12
d2=4.0
s2 ='is the best place to learn and practice coding!'
print(i+i1)
print(d+d2)
print(s+s2)'''

'''N = int(input().strip())
if N % 2 != 0:
    print("Weird") #this is wrong need to correct
elif 2 >= N <= 5:
    print("Not Weird")
elif 6 >= N <=20:
    print("weird")
elif N>20 :
    print("Not Weird")'''

# this is correct
# N = int(input().strip())
#
# if (N % 2 != 0) or (N >= 6 and N <= 20):
#     print("Weird")
# else:
#     print("Not Weird")


# l1 = [2, 4, 5, 6, 2, 2,9, 4, 5, 8, 6, 8]
# l2 = [] # unique
# l3 = [] # duplicate
# for i in l1:
#     if i not in l2:
#         l2.append(i)
#     else:
#         l3.append(i)
#         # l2.add(i)
# print(l2)
# print(l3)
# print(l1)

# check list having value or not
# l1 = []
# count = 0
# for i in l1:
#     count += 1
#     if count == 1:
#         print("print list having a value")
#     else:
#         print("no value")

# 2nd type to do the upervala program

# l = [2]
#
# if not l:
#     print("List is empty")
# else:
#     print("List having a value :", l)


# l = [1, 2, 4, 5, 6]
# l2 = []
#
# for i in l:
#     l2.append(i)
# print(l2)


# n = 3
# string1 = "The quick brown fox jumps over the lazy dog".split()
#
# l3 = []
# l4 = []
# for i in string1:
#     if len(i) > n:
#         l3.append(i)
#     else:
#         l4.append(i)
# print(l3)
# print(l4)


# def check_list_member(l1, l2):
#     if not l1:
#         return f'l1 having  no value:{l1}'
#     elif not l2:
#         return f'l1 having  no value:{l2}'
#     else:
#          return f'l1 having value:{l1}{l2}'
#
#
# print(check_list_member([],[]))


# def check_list_member(l1, l2):
#     result = False
#     for i in l1:
#         for j in l2:
#             if i == j:
#                 result = True
#                 return result
#
#
# print(check_list_member([1], [2]))
# print(check_list_member([4], [4]))

# def long_words(n, str1):
#     word_len = []
#     txt = str1.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len
#
#
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))


# l1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# first way
# l2 = l1.remove('Red')
# l4 = l1.remove('Pink')
# l3 = l1.remove('Yellow')
# print(l1)

# 2nd way
# print(l1[1:4])

# 3rd way
# l1.remove('Yellow')
# l2 = []
# for i in l1:
#     if i != 'Red' and i != 'Pink':
#         l2.append(i)
#
# print(l2)

# 4th way
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)


# l1 = [1, 2, 3, 4, 5, 6]
# l2 = []
# for i in l1:
#     if i % 2 != 0:
#         l2.append(i)
#
# print(l2)

# imp w3resources  question no. 15


# def printValues():
#     l = list()
#     for i in range(1, 21):
#         l.append(i ** 2)
#     print(l[:5])
#     print(l[-5:])
#
#
# printValues()

# t1 = list()
# n = 2
# for i in range(1, 31):
#     t1.append(i ** 2)
#
# print(t1[:5])
# print(t1[-5:])

#                prime no : no. is divided by itself and 1

# l1 = []
#
# l2 = []
# count = 1
# for i in range(1, 100):
#     if i / count == 1 and i / 1:
#         l1.append(i)
#
# count += 1
# print(l1)
# print(l2)


# l1 = int(input("lowest number"))
# h1 = int(input("highest number"))
# print("This are the prime number")
#
# for number in range(l1, h1 + 1):
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 break
#         else:
#             print(number)


# string method
# v1 = 20
# print("this is no {}".format(v1))


#                                      factorial
# while True:
#     num = int(input())
#
#     fact = 1
#
#     for i in range(1,
#                    num + 1):  # num + 1  beacause index start from 1 and we take 0 then it will multiply all output to 0
#         fact *= i
#
#     print(fact)


#                                      sum of square of N natural nos

# while True:
#     num = int(input("enter the value :"))
#     sum = 0
#
#     for i in range(num + 1):
#         square = i * i
#         print(square)
#         sum = sum + square
#     print("sum :", sum)
#


#                                     reverse the number


# num = 12345
#
# rev = 0
#
# while (num > 0):
#     remainder = num % 10
#     rev = (rev * 10) + remainder # this is th step where the main step of reverse the number
#     # rev store ramanider into the 54321 like revexample rev 0 then it became 5 then( rev*10+remainder ) = 5*10+ 4 = 50+4=54 and so on
#     num = num // 10
#
# print(rev)


#                                            reverse the string

# str1 = input("enter the string ").split()
# print(str1[-1])
# for i in list1:


# str1 = input("enter the string ")
#
# str2 = str1.split()
# for i in str2:
#     print()


# armstrong number
# Python program to check if the number is an Armstrong number or not

# while True:
#     num = int(input('enter the number:'))  # this are the armstrong number:  153 ,370 , 371,407
#     sum = 0
#
#     temp = num
#     while(temp > 0):
#         digit = temp % 10  # the method slice a digit one by one
#         sum += digit ** 3  # sum of digit and cube
#         temp //= 10  # remaining number  ex 153,15,1
#
#     if num == sum:
#         print("number is armstrong ")
#
#     else:
#         print('number is not armstrong')

# armstrong number in given range

# lower = 100
# upper = 100000
#
# for num in range(lower, upper + 1):
#
#     order = len(str(num))
#
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#
#     if num == sum:
#         print('this are armstrong number')
#         print(num)


# palindrome number

# while True:
#     num = int(input('enter the number'))
#
#     rev = 0
#     temp = num
#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num //= 10
#
#         if temp == rev:
#             print('Number is palindrome number ')
#         else:
#             print('numbe is not palindrome ')


# Fibonacci series

#  0, 1, 1, 2, 3, 5, 8, 13, 21,.......
#
# terms = int(input('Enter the number of terms u want:'))
# n1 = 0
# n2 = 1
#
# count = 0
#
# if terms <= 0:
#     print('Enter positive number')
# elif terms == 1:
#     print("Fibonacci sequence upto", terms, ":")
#     print(n1)
# else:
#     while terms > count:    # it will check the terms are grater than count
#         print(n1)
#         nth = n1 + n2
#
#         n1 = n2
#         n2 = nth
#         count += 1


# number is perfect or not


# num = int(input("please give a number: "))
# sum = 0
# for i in range(1, (num//2)+1):
#     remainder = num % i
#     if remainder == 0:
#         sum = sum + i
# if sum == num:
#     print("given input is perfect number")
# else:
#     print("given input is not a perfect number")


# number is perfect or not in given range

"""
for j in range(1, 200001):
    sum = 0
    for i in range(1, (j//2)+1):
        remainder = j % i
        if remainder == 0:
            sum = sum + i
    if sum == j:
        print("given input is perfect number", j)
        
 """
# ascending order number

# list1 = [1, 3, 4, 2, 6, 7, 5]  # 1
#
# for i in range(0, len(list1)):  # 0 (1),
#     for j in range(i + 1, len(list1)):  # 1(3),3(4),2(5)
#         if list1[i] >= list1[j]:  #
#             list1[i], list1[j] = list1[j], list1[i]
#             #      [4][3]      =      [3][4]
# print(list1)


# # descending order number
#
# list1 = [1, 3, 4, 2, 6, 7, 5]
#
# for i in range(0, len(list1)):
#     for j in range(i + 1, len(list1)):
#         if list1[i] <= list1[j]:
#             list1[i], list1[j] = list1[j], list1[i]


# LCM
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     greater = num1
# else:
#     greater = num2
# while (True):
#     if ((greater % num1 == 0) and (greater % num2 == 0)):
#         lcm = greater
#         break
#     greater += 1
# print("LCM of", num1, "and", num2, "=", greater)


# list1 = [1, 2, 3, 4, 5, 5]
# list2 = [2, 1, 2, 3, 4, 4]

# for i in list1:
#     if list1[1] == 2:
#         print(list1[1])
#     if list2[3] == 3:
#         print(list2[4])
#     else:
#         print('no')


#

#
# str1 = 'dheeraj'
# str2 = ''
# for i in range(len(str1) - 1, -1, -1):
#     print(str1[i], end='')
#
# print(str2)


# str1 = 'dheeraj'
# str2 = ''
# for i in range(len(str1) - 1, -1, -1):
#     str2 = str2 + str1[i]
# print(str2)


# str1 = 'dheeraj'
# str2 = ''
# count = 0
# for i in range(1, len(str1)-1):
#     if str1[i] == 'e':
#         count += 1
#
#
# print(count)


# str1 = 'dheeraj'
# count = 0
# str2 = ''
# for i in str1:
#     if i not in str2:
#         count += 1
#         str2 = str2 + i
#
# print(count)
# print(str2)


# str1 = 'dheeraj'
# for i in range(0, len(str1)):
#
#     if i % 2 != 1:
#         print(end='')
#     else:
#         print(str1[i])


# n = 'dheeraj'
# for i in range(0, len(n),2):
#     print(n[i:i+2],end=' ')


# list1 = ['D', 'h', 'e', 'e', 'r', 'j']
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
#
# print(list2)

# a = [1, 2, 44, 5, 6, 88]
# b = a[0]
# for i in a:
#     if i > b:
#         b = i
# print(b)

import random
import time

que = {1: "find min in list", 2: "find max in list", 3: "find sec max in list", 4: 'this_is_a_good=This.is',
       5: 'sort list asce', 6: 'sort list in desc', 7: 'palindrome no', 8: 'palindron string / list',
       9: '[123py34,56java,23c89]', 10: 'a=28$b=23$name=prakash=a:28 b:23 name:prakash', 11: 'count words in str',
       12: '[(ga(garry,harry,gama)]', 13: 'anagram or not', 14: 'remove duplicate from str', 15: 'a,a,a,b,b,a=a:4',
       26: 'count vowel + count in str', 16: '[101,102,100] remove zero', 17: 'find all substring',
       18: 'javabykisran = ja va by ki ', 19: 'Abcabc=abc count=2', 20: 'remove duplicate from list',
       21: 'reverse a string', 22: 'find longest common prefix', 23: 'prime no', 24: 'armstrong no',
       25: 'no is plindrome'}

q_no = [i for i in range(1, 27)]

a = q_no.copy()
while len(q_no) != 0:
    q = random.randint(1, len(a))
    if q in q_no:
        print(que[q])
        inp = input('Stop/Next : ').lower()
        if inp not in ['next', 'n']:
            time.sleep(2.5)
            q_no.remove(q)
        else:
            break