n=int(input())
s=0
for i in range(1,n+1):
    if n%i==0:
        s=s+i
j=s-n
if j==n:
    print("True")
else:
    print("False")