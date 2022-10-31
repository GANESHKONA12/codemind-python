n=int(input())
l=list(map(int,input().split()))
l=list(set(l))
cnt=0
for i in l:
    if i%2==0 and i!=0:
        cnt+=1
print(cnt)