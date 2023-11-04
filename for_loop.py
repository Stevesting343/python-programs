# for i in range(0,10): # (n-1) # there is an standard increment by 1
#     print("hii")
#

# iterables means countable or count one by one
num = 1200  # no.is not iterable

l = [1, 10, 20, 120, 50]  # list is iterable

s = "Dheeraj"  # string it also an iterable

t = (1, 10, 20, 120, 50)  # is Iterable

set = {1, 10, 20, 120, 50}  # iterable
# for variable in set:  # just change iterable data type 'l,string,tuple,set,dictionary' etc
#     print(variable)


# dic={
#     "key":"hii",
#     "key2":"hello",
#     "key3": "Dheeraj"
# }
# for variable in dic:
#     print(dic[variable]) # to find values inside the keys


#
# for i in range(1,11):
#     print(17,"x", i ,"=",i*17)

# for positive step value(star,end,step(is + or - ))

# for i in range(1,11,2):# there is not standard  increment so we use else in also for loop
#     print(17,"x", i ,"=",i*17)
# else:
#     print("loop has been stoped")

# for positive step value and it it is reverse table program
#
# for i in range(10,1,-1):# there is not standard  increment so we use else in also for loop
#     print(17,"x", i ,"=",i*17)
# else:
#     print("loop has been stoped")

# do the vowels program for a string

# sentence="hIi dhEeraj hello".lower() #we also write the lower() here
sentence = "hIi dhEeraj hello"
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in sentence:  # also we use here
    if i.lower() in vowels:
        count += 1  # it is count no of vowels in sentence
        print(i)

print(count)
