#O(n)
def fib(n,List):
    a,b=0,1
    List.append(a)
    while b<=n:
        List.append(b)
        a,b = b,a+b
n=int(input('n='))
L1=[]
fib(n,L1)
print(L1)