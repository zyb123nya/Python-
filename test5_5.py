import math
def var(L1):
    s,p = 0,0
    for i in range(len(L1)):
        v=L1[i]
        s+=v
        p+=v*v
    s=s/len(L1)
    mse=p/len(L1)-s*s
    return mse
L1=[5,3,7,8,14,9,12,6]
dx=var(L1)
print("方差为：%.2f"%dx)
mse=math.sqrt(dx)
print('标准差为：%.2f'%mse)
 