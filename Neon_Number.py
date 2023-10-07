n=int(input())
s=n*n
r=0
m=0
while s!=0:
    r=s%10
    s=s//10
    m=m+r
if(m==n):
    print("Neon Number")
else:
    print("Not Neon Number")