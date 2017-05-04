n=input("enter number")
i=2
f=1
for i in range(n/2):
    if(i!=0 and i!=1):
       if(n%i==0):
           f=0
           break;
if(f==1):
    print(str(n)+" is prime")
else:
    print(str(n)+" is not a prime")
