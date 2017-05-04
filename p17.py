import sys
n=input("enter size")
mat=[[0 for x in range(n)]for y in range(n)]
for i in range(n):
    for j in range(n):
        mat[i][j]=input()
for i in range(n):
    print
    for j in range(n):
        sys.stdout.write(str(mat[i][j])+str("\t"))
