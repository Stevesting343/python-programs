
#slicing the email having " . " with the user name

email = input("Enter the email:")
print(email)
user_name = email[0:email.index('@')]
raw_company_name = email[email.index('@'):] # at this step from @ to upto  " .com " email can slice
company_name = raw_company_name[raw_company_name.index('@')+1:raw_company_name.index('.')]
print("user_name:-" + user_name)
print("raw_company_name:-" + raw_company_name)
print("company_name:-"+company_name)

#for dhiraj.kadu@techamplifiers.com this type of email it will be the best program

#slicing a strin g
# word ="SuperExcited"
# # word[start:end:step] it count poisition like this 0,1,2,3,4,5 5 beacause we give 4 it will print upto "supe"
# # step is optional if need use it
#
# hii= word[0:5:2] # after giving step
#
# na= word[0:5]
#
# print(word[0:4])     # we also write in print()
# print(word[0:])
# print(word[:6])      # it will take bydefault 0
# print(word[:])
# print(word[::2])
# print(word[::-2])
# print(word[8:3:-1])  #print empty it first revers beacuse -1 and count reversly
# print(word[::2])
# print(hii)
# print(na)
# print(word[::-1])    #reverse the string

#hacker rank review challenge

# T=input()
# S="Hacker Rank"
# N=int(len(S))
# Count=0
# for i in range(0,T):
#
#     if N %2==0:
#         print()
#     else:
#         print()












