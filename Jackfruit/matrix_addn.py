a,b=map(int,input().split(" "))
m=[]
n=[]
s=[]
for i in range(a):
    row=list(map(int,input().split(" ")))
    m.append(row)
for i in range(a):
    row=list(map(int,input().split(" ")))
    n.append(row)    
print("First Matrix:")
for row in m:
    for v in row:
        print(v,end=" ")
    print()    

print("Second Matrix:")
for row in n:
    for v in row:
        print(v,end=" ")
    print()  
    

print("Sum of the two matrices is:")                
for i in range(a):
    row=[]
    for j in range(b):
        row.append(m[i][j]+n[i][j])
    s.append(row)
for row in s:
    for v in row:
        print(v, end=" ")
    print()    
        


