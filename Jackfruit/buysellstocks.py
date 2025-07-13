n=int(input())
a=list(map(int,input().split()))
profit=0
maxp=0
for i in range(n):
    for j in range(i,n):
        if i!=j:
            profit = a[j]-a[i]
            if profit>maxp:
                maxp=profit
print(maxp)        
