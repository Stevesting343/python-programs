# d1 = {0: 10, 1: 20} # add element to dictionary
#
# d1['2'] = 30
# print(d1)
# def merge(dic1, dic2):
#     return dic2.update(dic1)
#
#
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
#
# print(merge(dic1, dic2))
#
# print(dic2)


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def check(i):
    if i in d:
        print("key is present in the dictionary")
    else:
        print("key is not present in the list")


check(1)
check(7)



