a = int(input("enter the age "))
print(a)
if a <= 5 and a >= 1:
    print(" child")
elif a >= 18 and a < 58:
    print("adult")

elif a <= 18 and a > 5:  # we take this step at second elif
    print(" teen")

elif a >= 58:
    print("old")

else:
    print("age is not valid")
