def Count(my_string,char):
    count=0
    for i in my_string:
        if i == char:
            count+=1
    return count
my_string=input("enter the string :")
new_char=input("enter the charcter you want count :")
count=Count(my_string,new_char)
print("count character in {0} is :".format(my_string),count)