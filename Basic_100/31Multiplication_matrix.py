def Mat_mult(mat1,mat2):
    row1=len(mat1)
    col1=len(mat1[0])
    row2=len(mat2)
    col2=len(mat2[0])
    mat3=[]
    if row1 != col2:
        print("matrix multiplication is not possible")
        return 0
    elif row1 == col2:
        for i in range(row1):
            new=[]
            for j in range(row1):
                sum=0
                for k in range(col1):
                    sum+=mat1[i][k]*mat2[k][j]
                new.append(sum)
            mat3.append(new)
        return mat3
    else :
        return 0


mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[5,6,7],[8,9,7],[10,11,9]]
mat3=Mat_mult(mat1,mat2)
print("multiplication of matrixes is : ",mat3)