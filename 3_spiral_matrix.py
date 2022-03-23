columns=int(input())
rows=int(input())
matrix = [[int(input()) for x in range (columns)] for y in range(rows)]
print(matrix)
st_row_ind=0
st_col_ind=0
while(st_row_ind<rows and st_col_ind<columns):
    for i in range(st_col_ind,columns):
        print(matrix[st_row_ind][i],end=" ")
    st_row_ind+=1
    for i in range(st_row_ind,rows):
        print(matrix[i][columns-1],end=" ")
    columns=columns-1
    if(st_row_ind<rows):
        for i in range(columns-1,(st_col_ind-1),-1):
            print(matrix[rows-1][i],end=" ")
        rows-=1
    if(st_col_ind<columns):
        for i in range(rows-1,st_row_ind-1,-1):
            print(matrix[i][st_col_ind],end=" ")
        st_col_ind+=1
