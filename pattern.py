# Sqaure Pattern

# for i in range(0,6):
#     for j in range(0,6):
#         print("*",end=" ")
#     print()

# Right angled triangle

# for i in range(0,6):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# revese right angled triangle
#
# for i in range(0,6):
#     for j in range(i,6):
#         print("*",end=" ")
#     print()

#  left angled triangle
#
# for i in range(0,6):
#      for j in range(i,6):
#          print('',end="  ")  # it only space sheft in the program
#      for j in range(i+1):
#              print('*',end=" ")
#      print()


# reverse left side triangle
'''
  * * * * * * * * * * * 
    * * * * * * * * * 
      * * * * * * * 
        * * * * * 
          * * * 
            * 
                     '''

# for i in range(0,6):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,6):
#         print("*",end=" ")
#     for j in range(i,5):        # to join 2 triangles take the third loop and second side triangle logic
#             print("*",end=" ")
#     print()

#
'''         *
            * *
            * * *
            * * * *
            * * * * *
            * * * * * *
            * * * * *
            * * * *
            * * *
            * *
            *               '''
# for i in range(0,6):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(0,6):
#     for j in range(i,5):
#             print("*",end=" ")
#     print()

# plus  pattern

'''    *
       *
 *  *  *  *  *
       *
       * '''

for i in range(0, 5):
    for j in range(0, 5):
        if (i == 2) or (j == 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")  # logic also at spaces
    print()

# '=='comparison operator

# for i in range(0,6):
#     for j in range(i,6):# we take i because i changing and the range decrease by 1 cause i is varing
#         print("",end="  ") #we have to tak spaces as well in that right angle  ,triangle left side triangle we done
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(0, 6):
#     for j in range(1, 8):
#         if (i == 4) or ((i + j == 5) or (j - i == 3)):
#             print("*", end="")
#         else:
#             print(" ", end=" ")
#     print()
# if (i == 3) or (j == 3) and (i == 3) or ((j == 3) and (j == 4)) or ((i == 4) and (j == 2) or ((j == 3) or (j == 4))):
