n=int(input())
m=str(n)
m=m[::-1]
m=int(m)
c=0
d=0
for i in range(2,n):
    if n%i==0:
        c=1
for i in range(2,m):
    if m%i==0:
        d=1
if c==0 and d==0:
    print("circular prime")
elif c==0 and d!=0:
    print("prime but not a circular prime")
elif c!=0:
    print("not prime")