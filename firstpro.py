email = input("Enter the email:")
print(email)

user_name = email[0:email.index('@')]
# raw_company_name = email[email.index('@'):]
company_name = raw_company_name[raw_company_name.index('@') + 1:raw_company_name.index('.')]

company_name = email[email.index('@') + 1:email.index('.')]

print("user_name:=" + user_name)
print("company_name:=" + company_name)

# this is slicing type program to separate only no ' . ' in user name for that type of it will work
# dheearj@kadu.com
