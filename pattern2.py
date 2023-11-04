'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 '''

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1


'''

# for i in range(1,6):
#     for j in range(1,7-i):
#         print(j,end="")
#     print()
#
'''
     1 
    1 2 
   1 2 3 
  1 2 3 4 
 1 2 3 4 5
'''
# for i in range(1,6):
#     for j in range(1,7-i):
#         print(" ", end="")
#     for j in range(1,i+1):
#          print(j,end=" ")
#     print()


'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
'''
# for i in range(1,6):
#     for j in range(1,7-i):
#         print(" ", end="")
#     for j in range(1,i+1):
#          print("*",end=" ")
#     print()

'''
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
'''

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("",end=" ")
#     for j in range(1,7-i):
#         print("*",end=" ")
#     print()

'''
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
'''
# for i in range(1,6):
#     for j in range(1,7-i):
#         print("",end="  ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


'''
  1 2 3 4 5 
    1 2 3 4 
      1 2 3 
        1 2 
          1
'''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("",end="  ")
#     for j in range(1,7-i):
#         print(j,end=" ")
#     print()


'''
     1
    1 * 
   1 * 3
  1 * 3 * 
 1 * 3 * 5
 1 * 3 * 5
  1 * 3 * 
   1 * 3
    1 * 
     1

'''
# for i in range(1,6):
#     for j in range(1,7-i):
#         print("",end=" ")
#     for j in range(1,i+1):
#         if j==2 or j==4:
#             print(" *",end=" ")
#         else:
#             print(j,end="")
#     print()
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for j in range(1,7-i):
#         if j==2 or j==4:
#             print(" *",end=" ")
#         else:
#               print(j,end="")
#     print()

'''
     1 
    1 2 
   1 2 3 
  1 2 3 4 
 1 2 3 4 5 
  1 2 3 4 
   1 2 3 
    1 2 
     1

'''
# for i in range(1,5):
#     for j in range(1,7-i):
#         print("",end=" ")
#     for j in range(1,i+1):
#          print(j,end=" ")
#     print()
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for j in range(1,7-i):
#          print(j,end=" ")
#     print()


'''
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
    1 2 3 4 
      1 2 3 
        1 2 
          1 

'''
#
# for i in range(1,5):
#     for j in range(1,7-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#          print(j,end=" ")
#     print()
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(" ",end=" ")
#     for j in range(1,7-i):
#          print(j,end=" ")
#     print()

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 '''

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# for i in range(1,6):
#     for j in range(1,i+1):
#          print("",end="")
#     for j in range(1,7-i):
#         print(j,end=" ")
#     print()
'''
1 
2 2 
3 3 3 
4 4 4 4 
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
'''  # solve this another form below

# num=7
# for i in range(num):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(j,end=" ")
#         else:
#             print("*",end="")
#     print()
# for i in range(1,9):
#     for j in range(1,num-i):
#         if j % 2 != 0:                    #this part is  Not done yet
#             print(j,end=" ")
#         else:
#             print("*",end="")
#     print()


# another one
# n=6
# for i in range(n):
#     for j in range(n):
#         if (j%2)==0:
#             print(j,end="")
#         else:
#             print("*",end="")
#     print()

# hollow triangle
"""
     *   
    * *  
   *   * 
  *     *
*********
"""
for i in range(1, 5):
    for j in range(1, 8):
        if i + j == 5 or i == 4 or j - i == 3:
            print("*", end="")
        else:
            print("", end=" ")
    print()
