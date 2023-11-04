# program of factorial

# num = int(input("enter the value :"))
# factorial = 1
# if num < 0:
#     print("factorial doesnot exist for negative no.")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#  for i in range(1,num+1): # num + 1 is beacause it will count from (n-1) no. ex,4! 4+1 =5 it will stop
#   factorial = factorial * i
#  print("The factorial of", num, "is", factorial)# the step keep in the line of for loop beacause it will count
#                                                # till the step is incresing in loop

# program for print the table

# num = int(input('enter the no.'))
# for i in range(1,11):
#     print(f'table of {num} is',i*num)


# prime number = the number having only two divisor exaple 2,3,5  2(1,2), 3(1,3)

# a = int(input("enter the prime number"))
# for i in range(2, a // 2):
#     if a % i == 0:
#         print('not prime')
#         break
# else:
#
#     print('prime')


# perfect Number

# positive integer that is equal to sum of its positive divisors(6 = 1+2+3)


# num = int(input("enter the number"))
#
#
# # def perfect(num):
# sum1 = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum1 = sum1 + i
# if sum1 == num:
#     print("number is perfect")
# else:
#     print("number is not perfect ")
#
# # perfect(num)



# perfect number within range


# for num in range(1, 30):
#     sum1 = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum1 = sum1 + i
#
#     if sum1 == num:
#         print("number is perfect", sum1)
#     else:
#         print("number is not perfect")



