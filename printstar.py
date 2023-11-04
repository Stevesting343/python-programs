# for i in range(7):
#     for j in range(7):
#         if i==6 or j==0 or i==0 or j==6:
#             print("*",end=" ")
#         else :
#             print("1",end=" ")
#     print()
#
# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# for i in range(5):
#     for j in range(5-i):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(1,i + 1):
#             print("*", end=" ")
#     print()


#
# for i in range(5):
#     for j in range(5):
#         if i==2 or j==2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#

# for i in range(5):
#     for j in range(5):
#         if j==5 or i+j==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n= int(input())
# for i in range(n):
#     for j in range(n):
#         if i+j==3 or i==5 or j-i==3:
#              print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

for i in range(1, 5):
    for j in range(1, 8):
        if i == 4 or i + j == 5 or j - i == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()
