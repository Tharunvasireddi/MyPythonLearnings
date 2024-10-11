num1=int(input("enter the number :"))
num2=int(input("enter the number :"))
ch=input("choose the operand +,-,*,/ :")
if ch=="+":
    result=num1+num2
elif  ch=="-":
    result=num1-num2
elif ch=="*":
    result=num1*num2
elif ch=="/":
    result=num1/num2
print(result)
