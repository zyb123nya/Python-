def sushu(n):
    import math
    i,w=2,0
    if n<=1:
        w=1
    while i <=int(math.sqrt(n)) and w==0:
        if n%i==0:
            w=1
            break
        else:
            i=i+1
    return w
n= int(input('n='))
if sushu(n)==0:
    print("是素数")
else:
    print("不是素数")
