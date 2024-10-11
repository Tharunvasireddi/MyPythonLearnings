side1=int(input("enter the length of first side of triangle : "))
side2=int(input("enter thr length of second side of triangle : "))
side3=int(input("enter the length of third side of triangle : "))
s=(side1+side2+side3)/2
Area=(s*(s-side1)*(s-side2)*(s-side3)) **0.5
print("Area of the triangle is : ",Area)