# all methods of dictionary

# dicts = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# example
#  keys  : Values
# "brand": "Ford"

# dicts = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(dicts.keys())  # The keys() method will return a 'list' of all the values in the dictionary.
# print(dicts.values())  # The Valuse() method will return a 'list' of all the values in the dictionary.
#
# a = dicts.get("model")  # get 'values' from the
# print(a)
#
# dicts['name'] = 'Steve'  # add elements to dictionary
# print(dicts)
#
#
# print(dicts.items())  # The items() method will return each item in a dictionary, as ' tuples ' in a list.
#
#
# #
#
#
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# if "model" in thisdict:  # it check the model is in the dictionart with in operation
#     print("Yes, 'model' is one of the keys in the thisdict dictionary")
#
# thisdict.update({'year': 2033})       # from the method we update the values into the dictionary
# print(thisdict)
#
#
# # The pop() and del method removes the item with the specified key name:
#
# thisdict.pop('model')
# print(thisdict)
#
# del thisdict['brand']
# print(thisdict)


# Python - Loop Dictionaries method

# dicts = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for i in dicts:
#     print(i)

# output:
# brand
# model
# year

# dicts = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for i in dicts:
#     print(dicts[i])

# output:
# Ford
# Mustang
# 1964


# dicts = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x in dicts.values():
#     print(x)


# dicts = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
#
# for x in dicts.keys():
#     print(x)

# dicts = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x, y in dicts.items():
#     print(x, y)


# output :
# brand Ford
# model Mustang
# year 1964


# Copy a Dictionary methods

# a = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# b = a.copy()
# print(b)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)

# Nested Dictionaries method

# myfamily = {
#     "child1": {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Tobias",
#         "year": 2007
#     },
#     "child3": {
#         "name": "Linus",
#         "year": 2011
#     }
# }
# print(myfamily)


# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
#
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
#
# print(myfamily)


# accsess the items in nested dictionaries

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
#
# print(myfamily["child2"]["name"])

# The fromkeys() method returns a dictionary with the specified keys and the specified value.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict = dict.formkeys()


# dic1 = {"key1": 11, "key2": 12, "key3": 13}
#
# # for i in dic1:
# #     print(dic1[i])
#
# for i in dic1:
#     print(i)

# convert list into dictionary

list1 = ["a", "n", "c"]
dic1 = {}
counter = 1
for i in list1:
    dic1[i] = counter
    counter += 1
print(dic1)

'''
# Python3 code to demonstrate
# clearing list as dict. value
# using loop + clear()

# initializing dict.
test_dict = {"Akash": [1, 4, 3],
             "Nikhil": [3, 4, 1],
             "Akshat": [7, 8]}

# printing original dict
print("The original dict : " + str(test_dict))

# using loop + clear()
# clearing list as dict. value
for key in test_dict:
    test_dict[key].clear()

# print result
print("The dictionary after clearing value list : " + str(test_dict))
'''