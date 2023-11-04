#          'security bot project'
# create a list of users
# Ask the user to enter his name
# IF the name is present in the system or list allow  it to enter
# else  ask admin to add his name to the system or list
# if admin says yes then add the name into user list
# if the admin says No then don't add the name to the list
list = ['Dheeraj', 'Raj', 'Akshya', 'Rutvik']
getlist1 = str(list).lower()
a = input(" Please enter ur name")
for elements in list:
    if ((a) in (getlist1)):
        print("welcome")
        break
    else:
        print("not found")
        break

'''count = 0
while count > 0 :
    print("welcome")
    for b in range(0,5):
        print("hii")
else:
      for i in range(0,3):
        print("Wait we want to ask admin")'''
