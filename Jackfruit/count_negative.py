m=int(input())
n=int(input())
a=[]
count=0
for i in range(m):
    row=list(map(int,input().split(" ")))
    a.append(row)
a.sort()
for i in range(m):
    for j in range(n):
        if a[i][j]<0:
            count+=1
print(count)
