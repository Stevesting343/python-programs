'''n = int(input("enter the no.of rows :"))
for i in range(0, n):

   for j in range(0,i + 1):
       print("* ", end="")

   print() #It is at level of last for loop'''
# This is the example of print simple pyramid pattern
'''n = int(input("Enter the number of rows"))
# outer loop to handle number of rows
for i in range(0, n):
     # inner loop to handle number of columns
     # values is changing according to outer loop
     for j in range(0, i + 1):
          # printing stars
          print("* ", end="")

          # ending line after each row
     print()'''

# triangle pattern
'''n = int(input("enter the no.of rows :"))
k =2 * n - 2
for i in range(0,n):
     for j in range(0,k):
         print(end=" ")
     k = k-2
     for j in range(0,i+1):
         print("* " ,end = "  ")# the space in the ' end=" " ' can matter beacuse shape of the pattern depends on that
     print()'''

# half pyramid pattern
'''n = int(input("enter the no. of rows:"))

for i in range(n+1,0,-1): # at this step n+1 because it count according 01234for n=5
    for j in range(0, i-1):
        print("* ",end=" ")
    print()'''

# synatx: range(start,stop,step)

'''x = range(3, 20,2)

for n in x:
    print(n)'''
# output:3 5 7 9 11 13 15 17 19 "with difference of 2"

# right angle triangle
'''           j=0
        1
        1  2 
i=0     1  2  3
        1  2  3  4
        1  2  3  4  5

'''
# n = int(input("enter the rows :"))

'''for i in range(0,6):  # 0,1,2,3,4
     for j in range(i,-1,-1):  # for n=1 it will stop(1,0) 1+1=2 and 0+1=1 (start,stop,step)
         print(j+1,end=" ") # so j+1 =0+1 = 1
     print()'''

# Right angled triangle but same value at same row
'''     1 
        2 2 
        3 3 3 
        4 4 4 4 
        5 5 5 5 5 
        6 6 6 6 6 6'''

'''for i in range(1,6):
    for j in range(i+1,-1,-1):
        print(i+1,end=" ")
    print()'''
# it is all about depend on i value to connected with j
'''     1 
        1 2 
        1 2 3 
        1 2 3 4 
        1 2 3 4 5 '''

'''         1 
            2 2 
            3 3 3 
            4 4 4 4 
            5 5 5 5 5 '''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()

# print plus sign
'''         *
            * 
        * * * * *           # not done 
            *
            *            '''

#
'''         
*  *  *  *  *  
*  *  *  *  *  
*  *  *  *  *  
*  *  *  *  *  
*  *  *  *  * '''
# n=5
# for i in range(n):
#      for j in range(n):
#         print("*",end ="  ")
#      print()          #take the print in 2nd loop

'''     
* 
* * 
* * * 
* * * * 
* * * * * '''

# n=5
# for i in range(n):
#      for j in range(i+1):
#          print("*",end=" ")
#      print()

'''         
*  *  *  *  *  
*  *  *  *  
*  *  *  
*  *  
*  
      '''

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end="  ")
#     print()


# right sided triangle pattern

'''
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
'''
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

'''
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
'''
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#
#     print()

# for i in range(6):
#     for j in range(6 - i):
#         print("  ", end="")
#     for j in range(i + 1):
#         print("* ", end="")
#     for j in range(i):
#         print("* ", end="")
#     print()
# for i in range(6):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i, 6):
#         print("* ", end="")
#     for j in range(5-i):
#         print("*", end=" ")
#     print()

# holo square


'''
              * * * * * *
              *         *
              *         *
              *         *
              * * * * * *
'''
#


#


# for i in range(1, 8):
#     for j in range(1, 10):
#         if i + j == 6:
#             print("*", end="")
#         else:
#             print("", end="")
#         print()
# print()

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# for i in range(1, 6):
#     for j in range(i, 6):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for j in range(1,7-i):
#         print(j,end="")
#     print()

for i in range(1, 6):
    for j in range(1, 7 - i):
        print(j, end=" ")
    # for j in range(1,i+1):
    #     print(j, end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 7 - i):
        print(j, end=" ")
    print()


