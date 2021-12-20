for n in range(2,1001):
    total=1
    for i in range(2,n):
        if n%i==0:
            total += i
    if total==n:
        print(n)
        
