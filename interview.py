# palindrome number

# num = int(input("enter the value u want "))
# rev = 0
# temp = num
#
# while temp > 0:
#     rem = temp % 10
#     rev = rev * 10 + rem
#     temp //= 10
#
# if num == rev:
#     print("this is plaindrome number")
# else:
#     print("this is  not plaindrome number")


# armstrong number  153 ,1634

#
# num = int(input("enter the value u want "))
# sum1 = 0
# count1 = 0
# temp = num
#
# while temp > 0:
#     rem = temp % 10
#     count1 += 1  # sum1 = sum1 * 10 + rem
#     temp //= 10
# print(count1)
# temp = num
# sum1 = 0
# while temp > 0:
#     rem = temp % 10
#     sum1 += rem ** count1
#     temp //= 10
# print(sum1)
#
# if num == sum1:
#     print("this is armstrong number")
# else:
#     print("this is not armstrong")


# perfect number  =  the number is equal to sum of its positive divisors except(not the given number) itself.  ex. 6

# num = int(input("enter the value:"))
# sum1 = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum1 += i
# if sum1 == num:
#     print("perfect number ")
# else:
#     print("not perfect number ")


# prime number = the number is divsible by itself and 1

# l1 = []
# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         l1.append(i)
# print(l1)


# Fibonacci series

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
#         print(n1,end=" ")
#         nth = n1 + n2
#
#         n1 = n2
#         n2 = nth
#         count += 1


# max ,sec max

# l = [11,2,3,43,23]
#
# max = l[0]
#
# for i in l:
#     if i > max:
#         max = i
#
# print(max)
#
# # sec_max
#
# sec_max = l[0]
# for i in l:
#     if i > sec_max and i != max:
#         sec_max = i
# print('secmax',sec_max)


# min ,sec min

# l = [11,2,3,43,23]
#
# min = l[0]
# for i in l:
#     if i < min:
#         min = i
# print(min)
#
# sec_min = l[0]
# for i in l:
#     if i<sec_min and i != min:
#           sec_min = i
#
# print(sec_min)

# input s = 'abracadabra'
#         position = 5, character = 'k'   output  -- 'abrackdabra'


# var = 'abracadabra'
#
# a = ''
# for i in var:
#     if i == 'c':
#         i = "k"
#
#     a += i
# print(a)

# var = 'abracdbra'
# position = 5
# replacement_char = 'k'
#
# # Create the modified string
# new_var = var[:position] + replacement_char + var[position + 1:]
#
# print(new_var)

# d = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
#
# a =[]
#
# for i in d:
#     if i not in a:
#         a.append(i)
#
#
# print(a)


#  1 to 10 without using loop

# def adds(a):
#     if a <= 10:
#         print(a, end=" ")
#         adds(a + 1)
#
#
# adds(1)


# def iterate_string(text, index=0):
#     if index < len(text):
#         print(text[index], end=" ")
#         iterate_string(text, index + 1)
#
#
# # Call the recursive function to iterate over the string
# iterate_string("python")
#

# def iterate_string(text, index=0):
#     if index < len(text):
#         iterate_string(text, index + 1)
#         print(text[index])
#
# # Call the recursive function to iterate over the string
# iterate_string("python")


# a = '1011111110111111111'  # check longest continues where 1 output = 9
# b = a[0]
# count = 0
# max = 0
# for i in range(len(a)):
#
#     if a[i] == b:
#         # print(a[i], end=" ")
#         count += 1
#         if count>max:
#         # print(count)
#             max+=1
#     else:
#         # print(a[i])
#
#
#         count = 0
#
# print(max)

# a = '10111111011111111101'
# c = 0
# max = 0
# for i in a:
#     if i == '1':
#         c += 1
#         if c > max:
#             max += 1
#     else:
#         c = 0
# print(max)


# def perfect_num(a):
#     sum1 = 0
#     for i in range(1,a):
#         if a % i == 0:
#             sum1 += i
#     if sum1 == a:
#         print("perfect num")
#     else:
#         print(" not perfect num")
#
# perfect_num(6)


# def prime_num(a):
#     l = []
#     for i in range(2, a):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             l.append(i)
#     print(l)
#
#
# prime_num(100)

# def armstrong(num):
#     count = 0
#     temp = num
#     while temp > 0:
#         rem = temp % 10
#         count += 1
#         temp //= 10
#
#     print(count)
#     temp = num
#     sum1 = 0
#     while temp > 0:
#         rem = temp % 10
#         sum1 += rem ** count
#         temp //= 10
#     print(sum1)
#     if num == sum1:
#         print("armstrong number ")
#     else:
#         print("not armstrong number ")
#
#
# armstrong(1634)

# palindrome number
# num = int(input("number"))
# sum1 = 0
# temp = num
# while temp > 0:
#     rev = temp % 10
#     sum1 = sum1 * 10 + rev
#     temp //= 10
# print(sum1)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in l:
#     if i % 2 == 0:
#         pass
#     print(i)
# print("sdfsf")
# for i in l:
#     if i % 2 == 0:
#
#         print(i)

# for i in l:
#     print(i)
#     break




''' what is authentication :

   authentication is the process in which users identity where checked to provide accsess to the user 
   In authentication user is verified 
   In determines the user is valid or not 
   
   what is authentication :
   
   Authorization is the process in which users authorities where checked
   In authorization user is validated
   In determines the what do user have 
   
   what is superuser :
   superuser is First or powerful user of the system which handels the Django admin panel who having acsess of all 
   database operation like create, read, update, delete.
  
   what is architecture of django :
   Django is based on model, view, template  pattern which follows model, view ,controller architecture 
   the main difference between mvt and mvc is that controller part where handeled by the django itself.
   
   model : model is the database logic It help's to interact with database which provide option 
   to create read update and delete query records 
   
   view : It is used to execute the business logic and interact with model to retrieve data and render template
   
   template : In this file all frontend part handeled . it is the html file mixed with django(jinja) template language. 
   The files where generally written in html ,css , javascript .
   
   what is Python Virtual Environment :
   It is the tool which provide all  external dependency (pakages or libraries) which are not provided by python standard 
   library and also provide  isoalated enviroment for all different project 
   
   what is web application :
   IT is code or client server Software Application which user or client  (user interface ) runs on web browser.
    
   project directory:
   __init.py: it is an empty file which tells python that the current directory is treated as package 
   manage.py : It is an command line utility which is entry point to interact with django project
    having commands like runserver(to run development server) ,makemigrations(to generate migration files that represent the changes ) , 
    migrate(to apply changes to the database) , creatsuperuser .
    
   settings.py : s a configuration file for your Django project. It contains settings that control various aspects of your application,
    such as database settings, authentication, middleware, installed apps, and more.
   urls.py :     
   
   
   '''
