n=int(input())
count=0
a=list(map(int,input().split()))
for i in a:
    if a.count(i)>1:
        count+=1
if count>0:        
    print('true')
else:
    print('false')
        
