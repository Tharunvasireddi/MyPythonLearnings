def Anagram(my_string1,my_string2):
    sum1,sum2=0,0
    for i in my_string1:
        k=ord(i)
        sum1+=k
    for i in my_string2:
        k=ord(i)
        sum2+=k
    if sum1==sum2:
        return True
    else :
        return False
my_string1=input("enter the first string : ")
my_string2=input("enter the second string : ")
if Anagram(my_string1,my_string2):
    print("{0} and {1} are Anagrams".format(my_string1,my_string2))
else :
    print("{0} and {1} are not Anagrams".format(my_string1,my_string2))
    