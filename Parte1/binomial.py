def fatorial(n):
    ret=1
    while n>1:
        ret=ret*n
        n=n-1    
    return ret

def binomial(n,k):
    return (fatorial(n))/(fatorial(k)*fatorial(n-k))

n=float(input("n:"))
k=float(input("k:"))
print(binomial(n,k))
