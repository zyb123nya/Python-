import random
temp = int(input("猜数字游戏开始，请输入数字0-10："))
guess = temp 
num = random.randint(1,10)
while guess != num:
    if guess == num:
        break
    elif guess > num:
        print("较大")
    else:
        print("较小")
    temp = int(input("请重新输入猜测的数："))
    guess = temp
print("你猜对了！") 