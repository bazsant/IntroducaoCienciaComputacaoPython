def x(n,m):
    print('entrou')
    if n == m or m == 0:
        return 1
    else:
        return x(n-1,m) + x(n-1,m+1)

print(x(5,3))
