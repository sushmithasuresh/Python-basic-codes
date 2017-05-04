a=[1,3,4,6,3,2,8,12,15,-8]
mini=-9999
maxi=9999
for i in a:
    if(mini>a[i]):
        mini=a[i]
    if(maxi<a[i]):
        maxi=a[i]
