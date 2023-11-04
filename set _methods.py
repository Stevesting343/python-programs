# set method s


# add
'''
emp_name = {'dheeraj', 'raj', 'gaurav', 'Gaurav'}
print(emp_name)

emp_name.add('Depak kalal')
print(emp_name)
'''

# copy

'''
emp_name = {'dheeraj', 'raj', 'gaurav', 'Gaurav'}
emp_name1 = emp_name.copy()
print("This", emp_name1)
'''

# pop
'''
emp_name = {'dheeraj', 'raj', 'gaurav', 'Gaurav'}

emp_name.pop()
print(emp_name)

'''

# remove
'''
emp_name = {'dheeraj', 'raj', 'gaurav', 'Gaurav'}
print(emp_name)
emp_name.remove('dheeraj')# if we remove raj first and then we write dheraj inmstead of the raj it raj see again in set
print(emp_name)
'''

# update
# it having two sets

'''
a1 = {'mango', 'banana', 'apple'}
a2 = {'google', 'agile', 'microsoft'}

a2.update(a1)
print(a2)
'''

# union
# union is same as the update
'''

a1 = {'mango', 'banana', 'apple'}
a2 = {'google', 'agile', 'microsoft'}

a3 = a1.union(a2)
print(a3)
'''

# difference

a1 = {'mango', 'banana', 'apple'}
a2 = {'google', 'agile', 'microsoft'}

a3 = a1.difference(a2)  # it show the a1 values
print(a3)








