import sys
n=input("enter size")
mata=[[0 for x in range(n)]for y in range(n)]
matb=[[0 for x in range(n)]for y in range(n)]
matc=[[0 for x in range(n)]for y in range(n)]
print "enter matrix 1"
for i in range(n):
    for j in range(n):
        mata[i][j]=input()
print "enter matrix 2"
for i in range(n):
    for j in range(n):
        matb[i][j]=input()
for i in range(n):
    for j in range(n):
        matc[i][j]=mata[i][j]+matb[i][j]
print "\nmatrix a"
for i in range(n):
    print
    for j in range(n):
        sys.stdout.write(str(mata[i][j])+str("\t"))
print "\nmatrix b"
for i in range(n):
    print
    for j in range(n):
        sys.stdout.write(str(matb[i][j])+str("\t"))
print "\nresultant matrix"
for i in range(n):
    print
    for j in range(n):
        sys.stdout.write(str(matc[i][j])+str("\t"))
                
