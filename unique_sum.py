n=int(input())
x=list(map(int,input().split()))
s=set(x)
a=0
for i in s:
    a=a+i
print(a)