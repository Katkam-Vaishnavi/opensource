x=list(map(int,input().split()))

if x[2]<x[0]:
    print(0)
    
elif x[2]>=x[0]+x[1]:
    print(2)

else:
    print(1)
