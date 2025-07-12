n=int(input())
D1=list(map(int,input().split()))
N1=list(map(int,input().split()))
x=int(input())
p=0
s=0
D1.sort()
N1.sort(reverse=True)
for i in range(n):
    s=D1[i]+N1[i]
    if s>x:
        p=p+(s-x)*100
print(p)        
