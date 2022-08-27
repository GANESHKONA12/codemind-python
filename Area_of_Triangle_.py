a,b,c=map(int,input().split())
s=(a+b+c)/2
x=(s*(s-a)*(s-b)*(s-c))**(1/2)
print("%.2f"%x)