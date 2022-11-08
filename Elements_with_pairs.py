n=int(input())
l=list(map(int,input().split()))
for i in l:
    if len(l)%2!=0:
        l.append(0)
print(*l)