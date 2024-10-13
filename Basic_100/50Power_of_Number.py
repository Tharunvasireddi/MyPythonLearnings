def Power(base,pow):
    if pow == 0:
        return 1
    elif pow==1:
        return base
    else :
        fact=1
        for i in range(pow):
            fact=fact*base
        return fact
base=int(input("enter the number : "))
pow=int(input("enter the power of number (must be in postive) :"))
power=Power(base,pow)
print("result of {0} to the power {1} is :".format(base,pow),power)