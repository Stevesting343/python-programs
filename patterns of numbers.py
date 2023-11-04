# for i in range(1,10):
#     for j in range(1,7-i):
#         print(" ", end=" ")
#     for j in range(1, i+1):
#         if i % 2 == 1 :
#             print(j, end=" ")
#         else:
#             print("",end="")
#     print()


'''
                  1
              1   2   3
          1   2   3   4   5
      1   2   3   4   5   6   7
  1   2   3   4   5   6   7   8   9
      1   2   3   4   5   6   7
          1   2   3   4   5
              1   2   3
                  1

'''
# for i in range(1, 10, 2):
#     for j in range(1, 11 - i):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         print(j, end="   ")
#     print()
# for i in range(1, 10,2):
#     for j in range(-1, i + 1):
#         print("  ", end="")
#     for j in range(1, 9 - i):
#         print(j, end="   ")
#
#     print()



# 1st

# for i in range(1,6):
#     for j in range(1,7-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#2nd

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for j in range(1,7-i):
#         print(j,end=" ")
#     print()

# special

# for i in range(1,6):
#     for j in range(1,7-i):
#         print(" ",end="")
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()

for i in range(1,7):
    for i in range(1, i+1):
        print(" ",end="")
    for j in range(6-i,0,-1):
        print(j, end=" ")
    print()