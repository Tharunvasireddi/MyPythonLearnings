a=int(input("enter the value of quadratic coefficient : "))
b=int(input("enter the value of linear coefficiant : "))
c=int(input("enter the value of constant : "))
root1=(-b+(pow(b,2)-4*a*c)**0.5)/2*a
root2=(-b-(pow(b,2)-4*a*c)**0.5)/2*a
print("Roots of Quadratic equation are : ",root1," and ",root2)