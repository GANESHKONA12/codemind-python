n=int(input())
l=list(map(int,input().split()))
s=0
t=0
for i in l:
    if i%2==0:
        s+=i
for i in l:
    if i%2!=0:
        t+=i
print(abs(s-t))