# l = [1,3,4,0]
# l1 = [2,5,6,9]
# l2 = [3,7,2,3]
#                   # 1*2*3  3*5*7  4*6*2 0*9*3
# def twice(n,a,b):
#     return n * a * b
#
# x = map(twice,l,l1,l2) # it multiplies first no. of three lists
# print(list(x))         # get same output from the code like this [6, 105, 48, 0]
#
# print(list(map(twice,l,l1,l2))) # get same output from the code like this [6, 105, 48, 0]
#
# # pass only given paramter not extra
# #------------------------------------------------------
#
# def twice(n,a,b):
#     return n * a * b
#
# x = map(twice,[1,3,4,0],[2,5,6,9],[3,7,2,3] )
# print(list(x))         # we directly pass list inside it
# print(list(map(twice,[1,3,4,0],[2,5,6,9],[3,7,2,3])))
#       # convert it into list

# find the square  in online using map function
# do like this
lis = [2, 5, 3, 4]  # dont take variable name as built in data type name
print(list(map(lambda n: n ** 2, lis)))
# ----------

# or like this
# ----------
print(list(map(lambda n: n ** 2, [2, 5, 3, 4])))

# ---------
# without list it will show function  name and the mememory location
print((map(lambda n: n ** 2, [2, 5, 3, 4])))
