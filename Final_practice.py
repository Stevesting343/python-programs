# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# print("--------------------------------------------------")
# for i in range(1, 6):
#     for j in range(1, 7 - i):
#         print("", end="  ")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# print("--------------------------------------------------")
#
# for i in range(1, 6):
#     for j in range(1, 7 - i):
#         print("", end=" ")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# print("--------------------------------------------------")
# for i in range(1, 6):
#     for j in range(1, 7 - i):
#         print("", end=" ")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
# print("--------------------------------------------------")
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("", end=" ")
#     for j in range(1, 7 - i):
#         print("*", end=" ")
#     print()
# print("--------------------------------------------------")
#
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 3 or j == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# print("--------------------------------------------------")
#
# # triangle hollow
# for i in range(1, 6):
#     for j in range(9):
#         if i + j == 5 or j - i == 3 or i == 5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# print("--------------------------------------------------")
#
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or j == 1 or i == 5 or j == 5:
#             print("*", end=" ")
#         else:
#             print("  ", end="")
#     print()
#
# print("--------------------------------------------------")
#
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()
# for i in range(1, 5):
#     for j in range(1, 6 - i):
#         print("*", end="")
#     print()
#
# print("--------------------------------------------------")
#
# for i in range(1, 5):
#     for j in range(1, 7 - i):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(" ", end="")
#     for j in range(1, 7 - i):
#         print("*", end="")
#     print()
# print("--------------------------------------------------")

# armstrong number 153

# num = int(input("enter value"))
# count = 0
# temp = num
#
# while temp > 0:
#     rem = temp % 10
#     count += 1
#     temp //= 10
# print(count)
#
# temp = num
# sum1 = 0
# while temp > 0:
#     rem = temp % 10
#     sum1 += rem ** count
#     temp //= 10
# print(sum1)
#
# if num == sum1:
#     print("number is armstrong")
# else:
#     print("number is not armstrong")

print("--------------------------------------------------")

# prime number
#
# for i in range(2, 20):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

print("--------------------------------------------------")

# perfect number

# sum1 = 0
# for i in range(1,20):
#     for j in range(1, i):
#         if i % j == 0:
#             sum1 += j
#     print(sum1)

print("--------------------------------------------------")
# plaindrome


# num = int(input(" enter the values u want"))
# rev = 0
# temp = num
# while temp > 0:
#     rem = temp % 10
#     rev = rev * 10 + rem
#     temp //= 10
# print(rev)
#
# if rev == num:
#     print("palindrome")
# else:
#     print("it is not palindrome")

print("--------------------------------------------------")

# fibnacci

# nterms = int(input("enter how many terms u want:"))
# n1 = 0
# n2 = 1
# count = 0
# if nterms <= 0:
#     print("enter positive value ")
# elif nterms == 1:
#     print("this is 2nd term ", n2)
# else:
#     while nterms > count:
#         print(n1, end=" ")
#
#         nth = n1 + n2
#
#         n1 = n2
#         n2 = nth
#         count += 1
#     print()

# max

# a = [1, 22, 3, 43, 24]
# max1 = a[0]
# for i in a:
#     if i > max1:
#         max1 = i
# print(max1)
#
# sec_max = a[0]
# for i in a:
#     if i > sec_max or i != max1:
#         sec_max = i
# print(sec_max)


# min
# s = [1, 3, 2, 3, 1, 4, 55, 6]
#
# min1 = s[0]
# for i in s:
#     if i < min1:
#         min1 = i
# print("min:", min1)
#
# for i in range(len(s)):
#     for j in range(len(s)):
#         if s[i] < s[j]:
#             s[i], s[j] = s[j], s[i]
#
# for i in range(len(s)):
#     if i > min1:
#         print("sec_min:", s[i])
#         break

# acsending  number

# l1 = [1, 3, 5, 6, 3, 2]
#
# for i in range(len(l1)):
#     for j in range(len(l1)):
#         if l1[i] < l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
#
# print("asc:", l1)

# for i in range(len(l1)):
#     for j in range(len(l1)):
#         if l1[i] > l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
#
# print("desc:", l1)

# 1
# a = 'I joined college at 18 years of age'.split()  # output 18
# print(a)
# for i in a:
#     if i.isdigit():
#         print(i)

# 2remove zero [101,102,34]

l = [101, 102, 34]

for i in l:
    for j in l:
        if j == 0:
            l.remove(i)
        else:
            l.append(i)

print(l)
