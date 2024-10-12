def Palindrome(my_String):
    k=0
    for i in range(len(my_string)//2):
        if my_string[i]!=my_string[-1+k]:
            return False
        k-=1
    return True
my_string=input("enter a string : ")
if Palindrome(my_string):
    print("given string is palindrome ")
else :
    print("given string not a plaindrome")