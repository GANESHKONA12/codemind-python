n=int(input())
a=[]
c=0
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
for j in a:
    x=j
    cnt=0
    for k in range (1,x+1):
        if x%k==0:
            cnt+=1
    if cnt!=2:
        c+=1
print(c)