s=raw_input("enter string")
l=len(s)
c=0
for i in range(l):
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        c=c+1
print c
