# filter function
# age =[20,22,24,30,28,20,22]
# def filtr_fun(n):
#     if n <= 25:
#         return True
#     else:
#         return False
#
# x= filter(filtr_fun,age)  #filter(funcation name,iterrables )    (without '()' brackets)
# print(list(x))

print(list(filter(lambda a: a <= 25, [20, 22, 24, 30, 28, 20, 22])))
