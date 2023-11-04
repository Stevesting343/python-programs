# srting formatting and its BUilt methods/functions in


#
# # count()   : It will count no. of characters in given string
# name ="dheerAj"
# name = name.count("e")
# print(name)
#
# # upper() :   It will captilaize all the lettrs in given string
# name ="dheerAj"
# name = name.upper()
# print(name)
#
# # lower():  It will convert  string into small letter
# name ="dheerAj"
# name = name.lower()
# print(name)
#
# # capitalize()    :it capitalizes only first letter of a word
# name ="dheErAj "
# name = name.capitalize() # only a word
# print(name)
#
# #title: It will convert the string into according to writing rules like this{ Dheeraj Kadu} first letter in given all the words
# in capital form

#
# name ="dheerAj kadu"
# name = name.upper().title()  # at this position  firstly it will convert it into upper and then titlecase
# print(name)

# input from user
# name = input("name:").capitalize()
# print(name)


# eamail cha example
# name = input("enter the emailID:").lower()
# print(name)

# Boolean
# isupper(): use with name dot function name and it will give the output as True or False

# name = input("name:")
#
# print(name.isupper())
# print(name.islower())
# print(name.isalpha())
# print(name.isdigit())
# print(name.isalnum())


#  Find position
# name = input("name:")
#
# print(name.index('j'))
# # print(name.index('t')) # it will print only character in string otherwise shows an error and breaks continuity of program
# print(name.find('t'))# it will print(-1) instead of error and not break the continuity of the program
# #like this
# print(name.find("a"))

# remove letter
# removes un wanted things in string
# strip()
# name = input("name:")
# print(name.strip()) # the empty stripe remove the space befor string or after string
#
# print(name.strip('e'))# after giving remve val it will count space again
# # it will only remove the letter ar join to the first letter or last leter
# print(name.strip("dh"))
# print(name.strip("j."))
# print(name.lstrip()) # in terminal click  this button to count space of right side spaces " --> "
# print(name.rstrip()) # in terminal click  this button to count space of left side spaces " <-- "
#
#
