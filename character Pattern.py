# for i in range(6):
#     for j in range(i+1):
#         print(chr(j+65),end=" ")
#     print()

# for i in range(0,11,2):
#     for j in range(1,12-i):
#         print("",end=" ")
#     for j in range(i+1,):
#         print(chr(j+65),end=" ")
#     print()

# for i in range(0,7):
#     for j in range(0,11):
#         if i==0 or i==6 or j==0 or j==10:
#             print(chr(j+65),end="")
#         else:
#             print(" ",end="")
#     print()

# not working
# for i in range(11):
#     for j in range(11):
#         if i+j==6 or i-j==4:
#             print(chr(65),end="")
#         else:
#             print("  ",end="")
#     print()

# for i in range(0,9,2):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(0,11-i):
#         print(chr(65+j),end=" ")
#     print()
# for i in range(0,11,2):
#     for j in range(0,12-i):
#         print(" ",end="")
#     for j in range(0,i+1):
#         print(chr(65+j),end=" ")
#     print()

# for i in range(0,9,2):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(0,11-i):
#         print(chr(65+j),end=" ")
#     print()
# for i in range(0,11,2):
#     for j in range(1,12-i):
#         print(" ",end="")
#     for j in range(0,i+1):
#         print(chr(65+j),end=" ")
#     print()


# str1 = "pyhton"
# for i in range(len(str1)-1,-1,-1):
#     print(str1[i])
# print()

# str1='dheeraj'
# str2 =""
# count = 0
# for i in range(len(str1)-1):
#     if str1[i] not in str2:
#         str2 = str2+str1[i]
#     else:
#         print(str1[i])
# print()
#

# a = "Dheeraj"
# l = ''
# for i in a:
#     if i not in l:
#         l += i
# print(l)

d = "dheerraj"
l = {}
count =0
for i in d:
    if d[i] not in l:
        count+=1



    print(count,i)

# a = 'harry'
# l = ''
# d = {}
# for i in range(len(a)):
#     if a[i] in d:
#         d[a[i]] += 1
#     else:
#         d[a[i]] = 1
# print(d)

# questions == dhiraj ouutput -->  dh ir aj