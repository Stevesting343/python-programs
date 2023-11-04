# l2 = ['']
#
#
# def func(l1):
#     for i in l1:
#         if i not in l2:
#             l2.append(i)
#         else:
#             print('this is not a unique number :', i)
#
#
# func([1, 2, 3, 4, 5, 5, 6, 6])


# write a python to print histogram   for 2,3,6,5,
# ex
# @ @,
# @ @ @,
# @ @ @ @ @ @,
# @ @ @ @ @


# def histogram(num):
#     count = 0
#     for i in range(1, num+1):
#         if count < i:
#             print("@", end="")
#             count += 1
#         else:
#             print("", end="")
#
#     print()
#
#
# histogram(2)
# histogram(3)
# histogram(5)
# histogram(6)


# concatenates list into the string

# list1 = [1, 2.5,'abc', 4,'5']
#
# str1 = ''
# for i in list1:
#     str1 = str1 + str(i)
# print(str1)


#
# str = 'hello world' # olleh dlrow
#
# print(len(str))
#
#
# a = len(str)
# print(a)


# str1 = 'Python'
# count = 0
# for i in str1:
#     if i == 'P':
#         count += 1
#         print(i)
#     else:
#         print(count)

#      0123456

# # print index word  and position

# for i in range(len(str1)):
#     if str1[i] == 'P':
#
#         print(str1[i],i)
# str1 = len(str1)
# print(str1)


# p = 'Python'
# a = p.index("n")
# print(a)

#
# for i in range(len(p)-1,0,-1):
#     print(p[i])


# str1 = 'Python'
#
# for i in range(len(str1) - 1, -1,-1):  # (len =6 in index of python index starts form 0123456 -1 = 5 ,  at negative indexing index print only upto zero ,  reverse step -1
#     print(str1[i], i)

# for i in range(10, 0,-1):
#     print(i)


# ascending order number

# list1 = [1, 3, 4, 2, 6, 7, 5]  # 1
#
# for i in range(0, len(list1)):  # 0 (1),
#     for j in range(i + 1, len(list1)):  # 1(3),3(4),2(5)
#         if list1[i] >= list1[j]:  #
#             list1[i], list1[j] = list1[j], list1[i]
#             #      [4][3]      =      [3][4]
# print(list1)
#
#
# # descending order number
#
# list1 = [1, 3, 4, 2, 6, 7, 5]
#
# for i in range(0, len(list1)):
#     for j in range(i + 1, len(list1)):
#         if list1[i] <= list1[j]:
#             list1[i], list1[j] = list1[j], list1[i]


# str1 = 'This is greate'.split()    # by default output: ['this', 'is', 'greate']
# print(str1)
#
# str1 = 'This is greate'.split('  ')   # after given three spaces into the split output: ['This is greate']
# print(str1)

# str1 = 'pyhton'.islower()  # output : True
# print(str1)
#
# str1 = 'pyhton'.upper()  # output : PYTHON
# print(str1)
#
# a = [1, 2, 3, 4, 5, 6, 7]
# a = len(a)

# count number of digits in the number  (only one method to count number )

# while True:
#     num = int(input())
#     count = 0
#     while (num > 0):
#         num //= 10
#         count += 1
#     print(count)


# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".
# For numbers that are multiples of three and five, print "FizzBuzz".


#  if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     else:

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)

# Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.

# l1 = [19, 19, 1, 0, 5, 5, 5]
# count = 0
# count2 = 0
# for i in l1:
#     if i == 19:
#         count += 1
#     elif i == 5:
#         count2 += 1
#
# if count == 2 and count2 == 3:
#     print(True)
# else:
#     print(False)
#
# print("number of 19:", count)
# print("number of 5:", count2)

#  Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.


# str1 = 'hello world'
#
# for i in range(len(str1) - 1, -1, -1):
# # print(str1[i], end="")
#     if str1[3]:
#         str1[3] = 'a'
#
# print(str1)

# str1 = "T"
#
# print(len(str1)-1)
# str1 = 'INSTAGRAM'
# print(str1[5])

'''
index and  Slice in string 
# when to use ?

index : it use for retreive single element from string 
syntax :
    str1= 'INSTAGRAM' 
    print(str[0])
    
# when to use ?    

slice: it use to retrive between element 
syntax :
    str1='INSTAGRAM'
    print(str1[start_index : end_index])      # end  index print -1 index from string 
    
'''
# str1 = 'INSTAGRAM'
# print(str1[0:4])     # it will not print  ' A '  beacause indexing start from 0 .

# str2 = "Dheeraj"
# st1 = str2[0:7]
# print(st1)
# st1 = str2[-5:-2]
# print(st1)

#
# for i in range(3, 28):
#     print("Hello Coddy:", i)

# nums = eval(input())  # Don't change this line
# print(list(nums))
# new_nums = list(nums)

# nums = eval(input())  # Don't change this line
# new_nums = list(nums)
# calculate = [x**3 + 2 * x**2 + 5 for x in new_nums]
# print(calculate)

# nums = eval(input())  # Don't change this line
# new_nums = list(nums)
# new_nums = [x**3+2*x**2+5 for x in new_nums]
# print(new_nums)





nums = eval(input())  # Don't change this line

new_nums = [x**3+2*x**2+5 for x in nums]
print(new_nums)