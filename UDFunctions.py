#  User Defind Fuctions
# it is  bolck of organised and reusable

#
# def function_name():
#     print()
#     print("Dheeraj")
#
# # function_name()
#
# name="Dheeraj"
# print(name.count('D'))
# print(name.count('e'))

# -----------

# name = "Dheeraj"
# def count_alpha(check_char):         # parameters(a, b)
#     # check_char = input("enter the character to count")
#     count = 0
#     for i in name.lower():   # any code return in function that can be used multiple time by calling the function
#         if check_char in i:  # we write this code without function it run only once or we want run again and again
#             count += 1
#     print(count)
#     return 'hii dheeraj',20 # it will return or assign values to the function
#                              # we take 2 values it return in tuple
# # a=20
# count_alpha('e')    # we must write how many paramters we take arguments while calling function
# count_alpha('d')
# print(name)
# print(count_alpha('e'))   # for return we write inside print() and also pass the argument
# # print(count_alpha('a'))

# ----------------
# def pattern(k):
#
#         for i in range(1,k):
#             for j in range(1,k-i):
#                 print(j, end=" ")
#             print()
#
# pattern(5)
# print(pattern(5))  # suppose we not take return the code shows 'None'
# pattern(10)


# def pattern(k):
#     for i in range(1, k):
#         for j in range(1, i+1):
#             print(j, end=" ")
#         print()
#
#
# pattern(5)
# print(pattern(5))  # suppose we not take return the code shows 'None'
# pattern(10)


def pattern(k):
    for i in range(1, k):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()


# pattern(5)
# print(pattern(5))  # suppose we not take return the code shows 'None'
pattern(51)

# prime no.
# odd no.
# reverse the no.
# + sign patern
