n=int(input())
a=list(map(int,input().split()))
f=True
for i in range(n-1):
    if a[i]>a[i+1]:
        f=False
        break
print("true" if f else "false")
