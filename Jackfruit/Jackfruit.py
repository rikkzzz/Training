N,D=map(int,input().split())
st=list(map(int,input().split()))
m=0
s=0
st.sort(reverse=True)
for i in range(D):
    s=s+st[i]
    if s>m:
        m=s
print(m)            
           
