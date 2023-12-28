# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# print("--------------------------------------------------")
# for i in range(1, 6):
#     for j in range(1, 7 - i):
#         print("", end="  ")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# print("--------------------------------------------------")
#
# for i in range(1, 6):
#     for j in range(1, 7 - i):
#         print("", end=" ")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# print("--------------------------------------------------")
# for i in range(1, 6):
#     for j in range(1, 7 - i):
#         print("", end=" ")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
# print("--------------------------------------------------")
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("", end=" ")
#     for j in range(1, 7 - i):
#         print("*", end=" ")
#     print()
# print("--------------------------------------------------")
#
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 3 or j == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# print("--------------------------------------------------")
#
# # triangle hollow
# for i in range(1, 6):
#     for j in range(9):
#         if i + j == 5 or j - i == 3 or i == 5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# print("--------------------------------------------------")
#
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or j == 1 or i == 5 or j == 5:
#             print("*", end=" ")
#         else:
#             print("  ", end="")
#     print()
#
# print("--------------------------------------------------")
#
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()
# for i in range(1, 5):
#     for j in range(1, 6 - i):
#         print("*", end="")
#     print()
#
# print("--------------------------------------------------")
#
# for i in range(1, 5):
#     for j in range(1, 7 - i):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(" ", end="")
#     for j in range(1, 7 - i):
#         print("*", end="")
#     print()
# print("--------------------------------------------------")

# armstrong number 153

# num = int(input("enter value"))
# count = 0
# temp = num
#
# while temp > 0:
#     rem = temp % 10
#     count += 1
#     temp //= 10
# print(count)
#
# temp = num
# sum1 = 0
# while temp > 0:
#     rem = temp % 10
#     sum1 += rem ** count
#     temp //= 10
# print(sum1)
#
# if num == sum1:
#     print("number is armstrong")
# else:
#     print("number is not armstrong")

print("--------------------------------------------------")

# prime number
#
# for i in range(2, 20):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

print("--------------------------------------------------")

# perfect number

# sum1 = 0
# for i in range(1,20):
#     for j in range(1, i):
#         if i % j == 0:
#             sum1 += j
#     print(sum1)

print("--------------------------------------------------")
# plaindrome


# num = int(input(" enter the values u want"))
# rev = 0
# temp = num
# while temp > 0:
#     rem = temp % 10
#     rev = rev * 10 + rem
#     temp //= 10
# print(rev)
#
# if rev == num:
#     print("palindrome")
# else:
#     print("it is not palindrome")

print("--------------------------------------------------")

# fibnacci

# nterms = int(input("enter how many terms u want:"))
# n1 = 0
# n2 = 1
# count = 0
# if nterms <= 0:
#     print("enter positive value ")
# elif nterms == 1:
#     print("this is 2nd term ", n2)
# else:
#     while nterms > count:
#         print(n1, end=" ")
#
#         nth = n1 + n2
#
#         n1 = n2
#         n2 = nth
#         count += 1
#     print()

# max

# a = [1, 22, 3, 43, 24]
# max1 = a[0]
# for i in a:
#     if i > max1:
#         max1 = i
# print(max1)
#
# sec_max = a[0]
# for i in a:
#     if i > sec_max or i != max1:
#         sec_max = i
# print(sec_max)


# min
# s = [1, 3, 2, 3, 1, 4, 55, 6]
#
# min1 = s[0]
# for i in s:
#     if i < min1:
#         min1 = i
# print("min:", min1)
#
# for i in range(len(s)):
#     for j in range(len(s)):
#         if s[i] < s[j]:
#             s[i], s[j] = s[j], s[i]
#
# for i in range(len(s)):
#     if i > min1:
#         print("sec_min:", s[i])
#         break

# acsending  number

# l1 = [1, 3, 5, 6, 3, 2]
#
# for i in range(len(l1)):
#     for j in range(len(l1)):
#         if l1[i] < l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
#
# print("asc:", l1)

# for i in range(len(l1)):
#     for j in range(len(l1)):
#         if l1[i] > l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
#
# print("desc:", l1)

# 9
# a = 'I joined college at 18 years of age'.split()  # output 18
# print(a)
# for i in a:
#     if i.isdigit():
#         print(i)

# 10       remove zero [101,102,34]

list1 = [101, 102, 34]

# for i in range(len(list1)):
#
#     list1[i] = int("".join((str(list1[i]).split("0"))))
# print(list1)

# 11
a = ['123python34', '234java66', '3435cpp90']  # words = ['python','java','cpp'] no = [12334,23466,343590]

# word = []
# num = []
#
# s1 = word
# s2 = num
#
# for i in a:
#     s1 = ''
#     s2 = ''
#     for j in i:
#         if j.isalpha():
#             s1 += j
#
#         else:
#             s2 += j
#     word.append(s1)
#     num.append(s2)
#
# print(word, num)

# 12
# l1 = ['abc', 'aba', '121', '1341']  # first and last character or value is same then print it
# for i in l1:
#     if i[0] == i[-1]:
#         print(i)


# 13  'hello hi today is good day' count no of spaces'


# a1 = 'hello hi today is good day'
# c1 = 0
# for i in a1:
#     if i == " ":
#         c1 += 1
# print(c1)

# 14     count vowels and consonent in 'I joined college at eighteen years of age'

# a1 = 'I joined college at eighteen years of age'.lower()
#
# v = 0
# c = 0
# for i in a1:
#     if i in 'aeiou':
#         v+=1
#     else:
#         c+=1
#
# print(v,c)

# 15 using list comprehension print those words whose length is less than 5 string = "Practice Problems to Drill List Comprehension in Your Head."


# string = "Practice Problems to Drill List Comprehension in Your Head.".split()
#
#
# print([i for i in string if len(i) <=5])

# 16    print no of six in given range 1 to 100

# print([i for i in range(1,100) if '6' in str(i)])

# 17     a3b4j2  output aaabbbbjj

# str1 = 'a3b4j2'
#
# for i in range(len(str1)):
#     if str1[i].isdigit():
#         for j in range(0, int(str1[i])):
#             print(str1[i - 1], end=" ")
#         print()


# 18  a = {1: {'name': 'garry', 'marks': 23, 3: {'name1': 'jonny'}}, 2: {'name': 'harry', 'marks': 83, 'div': 'a'}} print key and values

# a1 = {1: {'name': 'garry', 'marks': 23, 3: {'name1': 'jonny'}}, 2: {'name': 'harry', 'marks': 83, 'div': 'a'}}
#
# for i in a1:
#     for j in a1[i]:
#         print(j, a1[i][j])
#     print()

# 19 'javabykiran' output ja va by ki ra n

#
# s1 = 'javabykiran'
# result = ' '.join(s1[i:i + 2] for i in range(0, len(s1), 2))
# print(result)


# s1 = 'javabykiran'
# for i in range(0,len(s1),2):
#     print(s1[i:i+2])
#


# 20 a={'A':a,B:b........upto z}

# print({chr(65+i):chr(97 + i) for i in range(0,26)})

# 21 l = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"] using

l = ["Alex", "Bob", "Carol", "Dave", "Flow", "Katie", "Nate"]

# print({l[i]: i + 1 for i in range(len(l))})

# 22 'hello,python' count total no of occurance in string output {'h':2,'e':1,'l':2...so on}

# p = 'hello,python'
#
# b = {}
# for i in range(len(p)):
#     count = 1
#     for j in range(i + 1, len(p)):
#         if p[i] == p[j]:
#             count += 1
#     if p[i] not in b:
#         b[p[i]] = count
# print(b)

# 23 string = "Practice Problems to Drill List Comprehension in Your Head."
# output - {'Practice': 8, 'Problems': 8, 'to': 2, 'Drill': 5, 'List': 4, 'Comprehension': 13, 'in': 2, 'Your': 4, 	'Head.': 5}


# string = "Practice Problems to Drill List Comprehension in Your Head.".split()
# print({i: len(i) for i in string})


# 24 a= 'This_Is_A_Good' output - tHIS_iS_a_gOOD

# a1 = 'This_Is_A_Good'
#
# a2 = ''
#
# for i in a1:
#     if i.isupper():
#         a2 += i.lower()
#     else:
#         a2 += i.upper()
# print(a2)


# 25 a='garry.hii,hello' output - garry,hii,hello


# a1='gaurav,hii,hello'
# a1=a1.split('.')
# a1=a1[::-1]
# a1=','.join(a1)
# print(a1)


# 26 s = 'aabbbbcc' out put -  a2b4c2

# s = 'aabbbbcc'
#
# a1 = ''
#
# for i in range(len(s)):
#     count = 1
#     for j in range(i + 1, len(s)):
#         if s[i] == s[j]:
#             count += 1
#
#     if s[i] not in a1:
#         a1 += s[i] + str(count)
#
# print(a1)

# 27  a='1011111110111111111' check longest continues where 1 output = 9

a1 = '10111111011111111101'
c = 0
max = 0
for i in a1:
    if i == '1':
        c += 1
        if c > max:
            max += 1
    else:
        c = 0
print(max)

# 28   my_str = "aaaaaabcdefgfffffffffffffaabbbffbbbbbfgbb" output longest sequence ou- 13

# 29
# 30
# 31 'this is a string '  --- output --  'this-is-a-string'

# 32 input s = 'abracadabra'  position = 5, character = 'k'   output  -- 'abrackdabra'
# s = 'abracadabra'
#
# s2 = ''
# for i in s:
#     if i == 'c':
#         s2+= 'k'
#     else:
#         s2+=i
# print(s2)

# 33

# 34  chris alan  output - Chris Alan
# s = 'chris alan' .title()
# print(s)

s = 'chris alan'.split()

# 34

# 39   Input - [1,1,1,1,2,2,3,3,3,3,4,5] Expected Output - [1, 2, 3, 4, 5]

# input = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
#
# l1 = []
#
# for i in input:
#     if i not in l1:
#         l1.append(i)
# print(l1)

# 40 print 1 to 10 no without using loop

# def add(a):
#     if a <= 10:
#         print(a,end=" ")
#         add(a+1)
#
#
# add(1)

# 41 Input - "aabdb"  Expected Output - "d"  Explanation - "a" and "b" appear twice and "d" appears only ones.


# D = {}
# str1 = "aabdb"
# for i in str1:
#     if i in D:
#         D[i] += 1
#     else:
#         D[i] = 1
#
#
#
# for i in D:
#     if D[i] == 1:
#         print(i)

# ----------------

# reverse
str1 = 'dheeraj'
print(str1[::-1])


# print(len(str1))
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