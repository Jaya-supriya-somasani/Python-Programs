rows=int(input("No of Rows : "))
columns=int(input("No of Columns : "))
matrix=[]

for i in range(rows):          
    a =[]
    for j in range(columns):      
         a.append(int(input()))
    matrix.append(a)

print("Matrix")
for i in range(rows):
    a=[]
    for j in range(columns):
        print(matrix[i][j],end=" ")
    print()
print()
transpose=[]
for i in range(columns):          
    a =[]
    for j in range(rows):      
         a.append(0)
    transpose.append(a)


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i]=matrix[i][j]

print("Transpose of Matrix : ")
for i in range(len(transpose)):
    a=[]
    for j in range(len(transpose[0])):
        print(transpose[i][j],end=" ")
    print()
