n=int(input())
s1=list(map(int,input().split()))
l=list(set(s1))
for i in range(len(l)):
    print(l[i],end=' ')