mat=[[1,3,4],[5,6,7],[8,9,10]]
row = len(mat[0])
trans=[]
for j in range(row):
    new=[]
    for i in range(len(mat)):
        new.append(mat[i][j])
    trans.append(new)
print("Transpose of matric is : ",trans)
