import math
num1 = int(input())
num2 = int(math.sqrt(num1))
for i in range(2,num2+2):
    if num1%num2 ==0:
        break
if i == num2+1:
    print("%s是素数"%num1)
else:
    print("%s不是素数"%num1)
