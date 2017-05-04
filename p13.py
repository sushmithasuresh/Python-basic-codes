r=input("enter range")
os=0
es=0
for i in range(r+1):
    if(i%2==0):
        es+=i
    else:
        os+=i
print "odd sum=",os
print "even sum=",es
