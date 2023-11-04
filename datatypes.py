# list types

#it is ordered,changeable/mutable or also repeatative

# start using [] square bracket

# same memeory location it chages it s value
# list=[1,"dheeraj",20,20.5,None,True]
# print(list)
# for i in list:
#     print(i)
list1=[(1,"dheeraj"),20,20.5,None,True] #at 0th index we append it will show error
print(list1)
print(id(list1))
list1.append(2)
print(list1)
print(id(list1)) # add at same memory location


# tuple type

# It is ordered,Non-changeable
# start using () Round bracket
#
tuple=(1,"dheeraj",20,20.5,None,True)
print(id(tuple))
print(tuple)
# tuple.append(2) #It will print error


#Set
# unordered,changeable
# it will can't take non-repeatative element
s={1,"dheeraj",20,20.5,None,True}
print(s)
s1={1,"dheeraj",20,20.5,None,True,1}
print(s1) # it not take 1 again


#Dictionaries
# ordered, changeable, before 3.6 it is unordered
# it can't repeat keys again
dic={'car':"BMW",
     'model':23482,
     12:'mycar'
     }
print(dic)
dic['car']="BMW is big"











