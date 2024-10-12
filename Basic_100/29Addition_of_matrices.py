mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[1,2,3],[4,5,6],[7,8,9]]
mat3=[]
row=len(mat1[0])
for i in range(len(mat1)):
    new=[]
    for j in range(row):
        new.append(mat1[i][j] + mat2[i][j])
    mat3.append(new)
print("Addition of two matrices is : ",mat3)        