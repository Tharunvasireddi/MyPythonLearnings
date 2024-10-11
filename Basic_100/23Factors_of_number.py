num=int(input("enter the number : "))
fact=[]
for i in range(1,num+1):
    if num%i==0:
        fact.append(i)
print("Factors of {0} are :".format(num),*fact)