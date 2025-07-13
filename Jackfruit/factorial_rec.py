def fact(n):
    if n==1:
        return n
    return n * fact(n-1)


n=int(input())

result = fact(n)

print(result)
 
