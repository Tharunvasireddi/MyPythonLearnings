def Count(my_string):
    list1=my_string.split()
    return len(list1)
my_string=input("enter the string :")
count_words=Count(my_string)
print("count of words in {0} is :".format(my_string),count_words)