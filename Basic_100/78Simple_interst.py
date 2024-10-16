def Simple_interst(P,T,R):
    S_i=(P*T*R)/100
    return S_i
T=int(input("enter the number of days : "))
R=float(input("enter the rate of interest :"))
P=int(input("enter the principal amount : "))
s_i=Simple_interst(T,R,P)
print("the simple interset is : ",s_i)