n=int(input())
l=list(map(int,input().split()))
s=[]
m=[]
for i in l:
    if i%2==0:
        s.append(i)
    else:
        m.append(i)
print(len(s),len(m))