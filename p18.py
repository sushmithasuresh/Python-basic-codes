import sys
n=input("enter size")
mat=[[0 for x in range(n)]for y in range(n)]
mat1=[[0 for x in range(n)]for y in range(n)]
for i in range(n):
    for j in range(n):
        mat[i][j]=input()
for i in range(n):
    for j in range(n):
        mat1[i][j]=mat[j][i]
print "original matrix"
for i in range(n):
    print
    for j in range(n):
        sys.stdout.write(str(mat[i][j])+str("\t"))
print "\ntransposed matrix"
for i in range(n):
    print
    for j in range(n):
        sys.stdout.write(str(mat1[i][j])+str("\t"))
