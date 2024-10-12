def Punctuations(my_string):
    emp=""
    for i in my_string:
        k=ord(i)
        if (k >= 65 and k<=90) or (k>=97 and k<=122) :
            emp=emp+i    
    return emp
string=input("enter the string : ")
emp=Punctuations(string)
print(emp)