def Capitalising(my_string):
    ascii=ord(my_string[0])-32
    new_string=my_string.replace(my_string[0],chr(ascii))
    return new_string
my_string=input("enter the string : ")
print(" After capitilising of first letter of {0} is :".format(my_string),Capitalising(my_string))