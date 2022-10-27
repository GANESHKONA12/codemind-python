a,b=map(int,input().split())
c=max(a,b)
while True:
    if a%c==0 and b%c==0:
        print(c)
        break
    c=c-1
