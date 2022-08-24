n=int(input())
l=list(map(int,input().split()))
x,y=map(int,input().split())
b=0
for i in l:
    if i<x or i>y:
        print(i,end=' ')
        b+=1
if b==0:
    print(-1)
    