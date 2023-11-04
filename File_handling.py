# f = open("testfor_filehandling.py") # it will just open file not perform any operation w r a + x
# print(f.read())
# f.close()          # closes the file


# this method perform open as well as close no need to open and close it auto close file

# syntax: with open('txt.py',encoding='utf-,modes) # if file encoding format is bydefault then no need to write it
# with open('hii1.py','x') as f:
#     print()
# with open('hii1.py') as a:
#     print(a.read())

# modes

# write

# with open('hii1.py','W') as f:
#     ##print(f.write("hii dk"))
#     # output is write the  hii dk in file and give count in terminal
#     f.write("\n follow me")  # if we write again new thing in that it Eraise all and write again

#append



# r = opens a file for reading( read file automatically)

# with open('hii1.txt','+w') as f:
#    # print(f.write("Dheeraj k"))
#    print(f.tell())
#    f.seek(0)     # we told  the progrm to read from starting position or index it will read otherwise it will contiue after the end positon of first output
#    print(f.tell())# we change our current (position) using the seek() method
#    print(f.read(7))
#    print(f.read(4))
#    print(f.read())

   # W

with open("hii2.txt",'+r') as f:
      print(f.tell())
      print(f.read())





#    (' + ')  we use only with any one mode like   +a


