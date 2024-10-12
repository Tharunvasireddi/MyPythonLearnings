def Binary(n,Bin,result):
    if n==0:
        result=0
        Bin+=str(n)
        return Bin
    elif n==1 :
        Bin+=str(n)
        return Bin
    else :
        result = n%2
        Bin+=str(result)
        return Binary(n//2,Bin,result)
num=int(input("enter the number : "))
Bin=""
Bin=Binary(num,Bin,0)
bin="0b"+Bin[::-1]
print("the binary of {0} is : ".format(num),bin)