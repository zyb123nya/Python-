# O(n^2)
def fun1(n):
    if n == 1:
        return n
    else:
        return n * fun1(n-1)
print(fun1(5))