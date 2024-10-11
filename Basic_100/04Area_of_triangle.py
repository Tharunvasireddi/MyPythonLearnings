side1=int(input("enter the length of first side of triangle : "))
side2=int(input("enter thr length of second side of triangle : "))
side3=int(input("enter the length of third side of triangle : "))
s=(side1+side2+side3)/2
Area=(s*(s-side1)*(s-side2)*(s-side3)) **0.5
print("Area of the triangle is : ",Area)

# functional programming
def area_of_triangle(side1,side2,side3):
    semi_perimeter = (side1+side2+side3)/2
    return (semi_perimeter * (semi_perimeter -side1) * (semi_perimeter -side2) * (semi_perimeter -side3)) ** 0.5