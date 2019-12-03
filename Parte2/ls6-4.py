def x(n):
    if n == 0:
        print(n)
    else:        
        x(n-1)
        print(n)

x(10)
