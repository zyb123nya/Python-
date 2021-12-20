def hcf(x,y):
    if x > y:
       smaller = y
    else:
       smaller = x
 
    for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           hcf = i
 
    return hcf
def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
 
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
 
    return lcm
 
num1 = int(input("第一个数为："))
num2 = int(input("第二个数为:"))
print("最大公约数为：",hcf(num1,num2),"最小公倍数为：",lcm(num1,num2))