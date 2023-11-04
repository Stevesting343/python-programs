S = input()

try:
   if S.isdigit():
      int_input = int(S)
      print(int_input)

   else:

       raise ValueError("Bad String")

except ValueError as ve:
    print(ve)
