# a = [1, 2, 3, 10, 2, 4, 2, 10, 2, 6, 4, 10]

# output -- [1,two,3,ten,two,4,two,ten,two,6,4,ten]
#
# for i in range(len(a)):
#
#     if i == 2:
#         a[i] = 'two'
#     elif i == 10:
#         a[i] = 'ten'
#
# print(a)
#
# str1 = 'hello,hii'
# output --- hii,hello

# print(','.join(str1.split(',')[::-1]))


# remiain to done
# str3 = 'This__IS__A__Good'.split('__')

# print('.'.join(str3))

# for i in str3:

#     if i == i.upper():
#         print(i)
#     print()

# vowels in the string

# d = "Dheeraj"
#
# for i in d:
#     count = 0
#     for j in i:
#
#         if j in ['a', 'e', 'i', 'o', 'u']:
#             count += 1
#
#         print(i)
#     print('==', count)

# s = ''
# a = 'hi hello bye'
# for i in range(len(a)):
#     c = 1
#     if a[i] in 'aeiou':
#         for j in range(i + 1, len(a)):
#             if a[i] == a[j]:
#                 c += 1
#         if a[i] not in s:
#             s += a[i] + ':' + str(c) + ' '
# print(s)


# s = 'a,a,a,a,b,b,b,b'.split(',')
# e = ''
# for i in range(len(s)):
#     c = 0
#     for j in range(i, len(s)):
#         if s[i] == s[j]:
#             c += 1
#     if s[i] not in e:
#         e += s[i] + ':' + str(c) + ' '
# print(e)

# s = 'hello'
# e = 'elloh'
# not done
# for i in range(len(e)):
#     for j in range(i+1,len(e)):
#         if e[j] in s:
#             print('True')
#         else:
#             print('False')


# find possible  all substring

#
# a = 'Dheeraj'
#
# for i in range(len(a)):
#
#     for j in range(i + 1, len(a)+1):
#         print(a[i:j])
#
#     print()
# print()


#
# str1 = 'a=28 & b=23 & name = prkash'.split('=')
#
# print(str1)


#
# str2 = 'abcabc'
# str3 = 'abc'
#
# count = 0
# for i in range(0,len(str2),3):
#     print(str2[i:i+3])
#     if str3 == str2[i:i+3]:
#         count += 1
# print(count)

# a = ['123python34', '234java66', '3435cpp90']
# words = []
# no = []
# words = ['python','java','cpp']
# no = [12334,23466,343590]
# s1 = no
# s2 = words
# for i in a:
#
#     s1 = ''
#     s2 = ''
#     for j in i:
#
#         if j.isdigit():
#             s1 = s1 + j
#
#         else:
#             s2 += j
#     words.append(s2)
#     no.append(s1)
# print(words, no)


# str1 = "hii, Gaurav .!!! ''"
#
# # str1 = "hii, Gaurav .!!! \""
# e = ''
# for i in str1:
#
#     if i not in ['!', '.', '"']:
#         e += i
# print(e)

# upper = ''
# lower = ''
# s1 = upper
# s2 = lower
# s3 =
# s1 = ''
# s2 = ''
# s2 = ''
# s4 = ''

# Count number of special chars, upper case , lower case and numbers present in a string

# a = '&shUJHdjj263737'
#
# s1 = ''
# s2 = ''
# s3 = ''
# s4 = ''
# for i in a:
#
#     if i.isdigit():
#         s1 += i
#
#     elif i.islower():
#         s2 += i
#
#     elif i.isupper():
#         s3 += i
#
#     else:
#         s4 += i
#
# print(s1,'number')
# print(s2,'lower')
# print(s3,'upper')
# print(s4, 'special')


# str1 = 'hello dk hii'.split()
# print(str1)
# words = 0
# chracter = 0
# for i in str1:
#     print(i)
#     words += 1
#     for j in i:
#
#         chracter += 1
# print(chracter)
# print(words)


# list1 = ['abc','aba','121']
#
# for i in list1:
#     if i[0] == i[-1]:
#         print(i)

#
# l = [1, 2, 3, 4, 5]
#
# # target = 9
# # output = 3,4
# t = 9
# for i in range(len(l)):
#
#     for j in range(len(l)):
#         if l[i] + l[j] == t:
#             print(i, j)

# list1 = [101,201,23]
# # output:[11,21,23]
#
#
#
# for i in range(len(list1)):
#
#     list1[i] = int(''.join(str(list1[i]).split("0")))
#
# print(list1)


# write a program to disaply number which are divisible by 11 but not by 2 between 100 and 500


# for i in range(100, 501):
#
#     if i % 11 == 0 and i % 2 != 0:
#         print(i)


# a = frozenset({1,2,3,4})
# print(a)
# for i in range(len(a)):


# list comprehensions

#
# add = lambda x: (lambda y: x + y)
# a1 = add(10)
# print(a1(20))


#
# print([i for i in range(1,1000)])

# print([i for i in range(1, 1000 + 1) if i % 8 == 0])

## number of 6 in the given range

# print([i for i in range(1, 1000 + 1) if '6' in str(i)])

## count the number of spaces in string

# string = "Practice Problems to Drill List Comprehension in Your Head."
# for i in string:
#     print(i)
# #
# print(len([i for i in string if i == ' ']))
# print(len([i for i in range(len(string)) if string[i] == ' ']))
#
#
# print(''.join([i for i in string if i not in 'aeiou']))

# string = "Practice Problems to Drill List Comprehension in Your Head.".split()
# print([i for i in string if len(i) <= 5])

# string = "Practice Problems to Drill List Comprehension in Your Head.".split()
# print({i: len(i) for i in string})

# dictionary comprehension

# using random module

# import random
#
# customers = ["Alex", "Bob", "Carol", "Dave", "Flow", "Katie", "Nate"]
#
# print({i:str(random.randrange(1,100+1))+'$' for i in customers})
#
# l = ["Alex", "Bob", "Carol", "Dave", "Flow", "Katie", "Nate"]
#
# # print({l[i]: i + 1 for i in range(len(l))})
#
#
# print({chr(65+i): chr(97+i) for i in range(26)})
#
#
#
#
# # set comprehension
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print({i*6 for i in range(1,len(list1)) if list1[i] < 7})

# a = {1: {'name': 'garry', 'marks': 23,3:{'name':'jonny'}}, 2: {'name': 'harry', 'marks': 83, 'div': 'a'}}
#
# # for i in a:
# #     print(i)
# # print()
# for i in a:
#     for j in a[i]:
#         print(j,a[i][j])
#     print()


# a = {1: {'name': 'garry', 'marks': 23, 3: {'name1': 'jonny'}}, 2: {'name': 'harry', 'marks': 83, 'div': 'a'}}
#
# for i in a:
#     for i,j in a[i].items():
#         if type(j) == dict:
#             for i in j:
#                 print(i,':',j[i])
#         else:
#             print(i,':',j)


a = "a3b4h4k2"
# 'aaa bbbb hhhh kk'


c1 = ''
c2 = ''

# for i in range(1,len(a)):
#     if a[i].isdigit():
#
#
#         for j in range(0,int(a[i])):
#
#             print(a[i-1], end="")
#         print()
# print()


# gk program


# a="a3b4h4hk2"
# for i in range(len(a)):
#     if a[i].isdigit():
#         for j in range(int(a[i])):
#             print(a[i-1],end='')

# b = ''
# for i in a:
#     if  i.isalpha():
#         d = i
#     elif i.isdigit():
#         b += d*int(i)
# print(b)


# palindrome number


# armstrong


# Fibonacci
# prime Number

# prime number = the number having only two divisor exaple 2,3,5  2(1,2), 3(1,3)

# a = int(input("enter the prime number"))
# for i in range(2, a // 2):
#     if a % i == 0:
#         print('not prime')
#         break
# else:
#
#     print('prime')

# prime number
# l = []
# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         l.append(i)
# print(l)

# perfect Number

# num = int(input("t"))
# sum = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum += i
# print('s', sum)
#
# if num == sum:
#     print('number is perfect')
# else:
#     print("not perfect")


# 1st max , second 2nd max
# ascending and descending from list
#
l = [12, 3, 4, 5, 6, 74, 335, 677, 23]
#
# min = l[0]
#
# for i in l :
#     if i < min:
#         min = i
# print('min',min)

########################
#
# l2=[]
# max = l[0]
# for i in l :
#     if i > max:
#         max = i
#         l2.append(i)
# print('max',max)

########################

# sec_max = l[0]
# for i in l :
#     if i > sec_max and i != max:
#         sec_max = i
# print('secmax',sec_max)

######################

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]:
#             l[i],l[j] = l[j],l[i]
# print('descending',l)


##################

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j] = l[j],l[i]
# print('ascending',l)

#####################
'''

min = l[0]
for i in l:
    if i < min:
        min = i

print('min:', min)

sec_min = l[0]

for i in l:
    if i < sec_min and i != min:
        sec_min = i

print('sec_min:', sec_min)

'''

# nterms = int(input("terms t"))
#
#
# n1 = 0
# n2 = 1
# count = 0
# if nterms < 0:
#     print("enter positive terms")
# elif nterms == n1:
#     print("this is first terms", n1)
# else:
#
#     while nterms > count:
#         print(n1)
#         nth = n1 + n2
#
#         n1 = n2
#         n2 = nth
#         count += 1


'''
# asecnding 
a1 = [3, 2, 5, 2, 1]
for i in range(len(a1)):

    for j in range(i + 1, len(a1)):
        if a1[i] > a1[j]:
            a1[i], a1[j] = a1[j], a1[i]

print(a1)
'''
'''

# descending order 

a2 = [1, 2, 5, 3, 45]

for i in range(len(a2)):
    for j in range(i + 1, len(a2)):
        if a2[i] < a2[j]:
            a2[i], a2[j] = a2[j], a2[i]


print(a2)


'''

'''
num = int(input("enter value "))
temp = num
count = 0

while temp > 0:
    rem = temp % 10
    count += 1
    temp //= 10

sum1 = 0
temp = num
while temp > 0:
    rem = temp % 10
    sum1 += rem ** count
    temp //= 10

print(sum1)
if sum1 == num:
    print("this is armstrong number ")
else:
    print("this is not armstrong number ")
    
'''

''' # using function armstrong number
def armstrong(number):
    count = 0
    temp = number

    while temp > 0:
        rem = temp % 10
        count += 1
        temp //= 10
    temp = number
    sum1 = 0
    while temp > 0:
        rem = temp % 10
        sum1 += rem**count
        temp //= 10

    if number == sum1:
        return True
    else:
        return False


num = int(input("enter the value u want :"))

if armstrong(num):
    print("this is armstrong number")
else:
    print("this is not armstrong number")
    '''

'''
str1 = 'a3b2c3d6'
str2 = ''
for i in range(len(str1)):
    if str1[i].isdigit():
        for j in range(int(str1[i])):
            print(str1[i - 1])
            str2 += str1[i - 1]
        print()
print(str2)
'''

'''
num = 1234
temp = num
sum1 = 0
while temp > 0:
    rem = temp % 10
    print(rem)
    temp //= 10
'''

'''
num = int(input("enter any number"))
sum1 = 0
for i in range(1, num):
    if num % i == 0:
        sum1 += i
        
print(sum1)

if num == sum1:
    print("this perfect number")
else:
    print("this not perfect number")
'''

# num = [101, 102, 304]
# for i in range(len(num)):
#     num[i] = int(''.join(str(num[i]).split('0')))
# print(num)


# palindrome

# num = int(input("enter the number uwant :"))
#
# rev = 0
#
# temp = num
# while temp > 0:
#     rem = temp % 10
#     rev = rev * 10 + rem
#     temp //= 10
# print(rev)
# if num == rev:
#     print("this is plaindrome", rev)
# else:
#     print("not")
#

# armstrong
#
# num = int(input("enter the value:"))
#
# sum1 = 0
# count = 0
# temp = num
# while temp > 0:
#     rem = temp % 10
#     count += 1
#     temp //= 10
#
# print(count)
# sum1 = 0
# temp = num
# while temp > 0:
#     rem = temp % 10
#     sum1 += rem ** count
#     temp //= 10
# print(sum1)
#
# if num == sum1:
#     print("this is armstrong")
# else:
#     print("this is not armstrong number")


# perfect number
#
# num = int(input("enter the value:"))
# sum1 = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum1 += i
# if sum1 == num:
#     print("perfect number ")
# else:
#     print("not perfect number ")

# prime number

#
# l1 = []
# for i in range(1, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         l1.append(i)
# print(l1)

# asec

# l1 = [1, 2, 3, 25, 65]

# aesc
# for i in range(len(l1)):
#     for j in range(i+1, len(l1)):
#         if l1[i] > l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
#
# print(l1)

# desc
# for i in range(len(l1)):
#     for j in range(i+1, len(l1)):
#         if l1[i] < l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
#
# print(l1)


# first max

# l2 = [1, 2, 3, 25, 65]
# max = l1[0]
# for i in l2:
#     if i > max:
#         max = i
# print(max)
#
# sec_max = l1[0]
#
# for i in l1:
#     if i > sec_max and i != max:
#         sec_max = i
#
# print(sec_max)


# first min

# l1 = [1, 2, 3, 25, 65]

# min = l1[0]
# for i in l1:
#     if i < min:
#         min = i

# print('min:', min)

# sec_min = l1[0]

# for i in l1:
#     if i < sec_min and i != min:
#         sec_min = i

# print('sec_min:', sec_min)


# l1 = [1,23,1,2,1,3]

# max = l1[0]

# for i in l1:
#     if i > max:
#         max = i
# print(max)

# sec_max = l1[0]

# for i in l1:
#     if i > sec_max and i != max:
#         sec_max = i
# print(sec_max)

# first min and second min

l1 = [1, 3, 2, 5, 4]

#
min = l1[0]
#
# for i in l1:
#     if i < min:
#         min = i
# print(min)
#
#
#
# for i in range(len(l1)):
#     for j in range(i,len(l1)):
#         if l1[i] > l1[j]:
#             l1[i],l1[j] = l1[j],l1[i]
#
#
# for i in range(len(l1)):
#     if i>min:
#         print(i)
#         break


# tricky questions python

# 1
# a2 = {}
#
# print(type(a2))

# output : <class 'dict'>

# 2
# print(-10//3)
# output : -4 floor division choose lesser value i.e -3  is greater than -4

# print(10//3)
# 3 is less than 4 output is 3

# 3
# ouput like this : """conversation - He said ,"shantanu's explantion is very good and "I subscribed the channels"""

# print("\"\"\"conversation - He said ,\"shantanu's explantion is very good and \"I subscribed the channels\"\"\"")


# 4

# print(2**3**2) # by rule of right to left for exponent is 3square first and that value become 9 called exponent and base 2 and power of 2 raise to 9 = 512

# output :512


# 5

#  "python uses \n for newline"

# print("\"python uses \\n for newline\"")

# 6

# output : /\/\/\/\/\/\

# print("/\\/\\/\\/\\/\\/\\")

# 7

# name = "Dheeraj"

# print(name[2:8:-2])
# output it will print nothing because direction is positive and step value is negative and step interger -2 not find anything

# # print(name[8:2:-2])

# 8
# my_dict = {'jay': 32, 'viru': 54, 'jay': 43}  # it was override the same name keys according to python rule
# print(my_dict)
# print(len(my_dict))

# 9

# a1 = [1, 2, 3]
# b1 = [4, 5, 6]
# c1 = [7, 8, 9]
#
# # print output :- [(1, 2, 3),(4, 5, 6),(7, 8, 9)]
# print(list(zip(a1, b1, c1)))

# 10

# print(10.0 // 3) # if any number in division is in floating point then the answer is in floating
# print(10 // 3.0)

# 11
# num = 2E3  # 2 to the exponent of (E ,e = 10 power of 3 = 1000.0) 2 x 1000.0 = 2000.0 exponent comes in class float
# print(num)
# print(type(num))
# num1 = 2e4
# print(num1)
# print(3e4)

# 12

# for i in 763 < 1:
#     print(i)
# output : TypeError: 'bool' object is not iterable

# 13

# python allocate same memory location for same content
# a3 = 10
# print(id(a3))
# b = 10
# print(id(b))
# ## for list it will not print same memory location for list type
# b1 = [1,2,3]
# print(id(b1))
#
# c1 =[1,2,3]
# print(id(c1))


# remove duplicate from list

# lis1 = [1,2,3,4,2,1,3]
# #lis1 = ['h','e','l','l','o']
# lis2 = []
# for i in lis1:
#     if i not in lis2:
#         lis2.append(i)
# print(lis2)

# find all possible strings form

s = 'Dheeraj'

# for i in range(0,len(s)):
#     for j in range(i+1,len(s)+1):
#         print(s[i:j],end=" ")
#     print()

'''
D Dh Dhe Dhee Dheer Dheera Dheeraj 
h he hee heer heera heeraj 
e ee eer eera eeraj 
e er era eraj 
r ra raj 
a aj 
j 
'''

# list1 = [0,1,2,0,4,3]

# for i in list1:
#     if i == 0:
#         list1.remove(i) # when we remove it will delete
#         list1.append(i) # but we append it again then it goes last position

# print(list1)

# a = "dh ee ra j"
# for i in range(len(a)):
#     if a[i] != ' ':
#         print(a[i],end="")


# a = [1, 2, 3, 10, 2, 4, 2, 10, 2, 6, 4, 10]

# for i in range(len(a)):
#     if a[i] == 2:
#         a[i] ='Two'
#     elif a[i] == 10:
#         a[i] = 'Ten'
# print(a)       


# a = 'hello,hii'.split(',') # output: hii,hello

# print(','.join(a[::-1])) # two lines code same output

# print(','.join(a.split(',')[::-1]))     # one lines code same output

# first priority to the inside join round bracket operations then outside


# a = 'This__IS__A__Good'
# print('.'.join(a.split("__")))


# a = 'THIS IS GOOD'
# result = a.title()
# print(result)


# a = 'sky is blue'.split()
# print(' '.join(a[::-1]))

# a1 = [1, 2, 2, 3, 4, 5, 5, 5, 6, 6]  #want output in same list [1,4]
# a2 = []
# for i in range(len(a1)):
#     if a1[i] == 1 or a1[i] == 4:
#         a2.append(a1[i])
#
#
# print(a2)


# a1 = [1, 2, 2, 3, 4, 5, 5, 5, 6, 6]
# l1 = a1.copy()
# a2 = []
# for i in range(len(l1)):
#     if l1[i] == 1 or l1[i] == 4:
#         a2.append(l1[i])
#     else:
#         a1.remove(l1[i])
# print(a1)

# seprate the alphabet and character  from the list in sorted form  like this " ABR 237 "


# c = 'A7B3R2'
# r = []
# m = []
#
# for i in range(len(c)):
#     if c[i].isalpha():
#
#         r.append(c[i])
#     else:
#         m.append(c[i])
#
#
# l = r[0]
# for i in range(len(r)):
#     for j in range(len(r)):
#         if r[i] < l:
#             r[i], r[j] = r[j], r[i]
# print(r)
#
# l1 = m[0]
# for i in range(len(m)):
#     for j in range(len(m)):
#         if m[i] < l1:
#             m[i], m[j] = m[j], m[i]
# print(m)
#
# o1 = ''.join(r)
# print(o1)
# o2 = ''.join(m)
# print(o2)

# s1 = ['B', 'A', 'C', 'V']
# l = s1[0]
# for i in range(len(s1)):
#     for j in range(len(s1)):
#         if s1[j] > l:
#             s1[i], s1[j] = s1[j], s1[i]
# print(s1)

# a1 = []
# for i in range(10):
#     a1.append(i * ++i)
# print(a1)
# for a1[i] in a1:
#     print(a1[i])

# gusess

# list1 = [1]
# print(type(list1))
# if list1:
#     print(True)
# else:
#     print(False)


#
# str1 = 'aabdb'
# a1 = []
# a2 = []
# a4 = []
# for i in range(len(str1)):
#     if str1[i] not in a1:
#         a1.append(str1[i])
#     else:
#         a2.append(str1[i])
#
#
# print(a1, a2)
#
# for i in range(len(a1)):
#     if a1[i] not in a2:
#         a4.append(a1[i])
# print(a4[0])

# str2 = 'aabdb'
#
# dic1 = {}
#
#
# for i in range(len(str2)):
#         if str2[i] not in dic1:
#             dic1[i] += 1
#         else:
#             dic1[i] = 1
#
# print(dic1)

# a2 = ''
# for i in range(len(str1)):
#     if str1[i] == 'd':
#         a2 += str1[i]
# print(a2)

str1 = 'aabdb'


# l1 = []

# couter = 1
# for i in range(len(str1)):
#     dice[i] = couter
#     couter += 1
# print(dice)
