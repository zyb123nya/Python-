L = []
a = 0 #优的人数
b = 0 #良的人数
c = 0 #中的人数
d = 0 #及格的人数
e = 0 #不及格的人数
for i in range(10):
    k = input("请输入第{}位学生的成绩:".format(i+1))
    L.append(k)
for j in L:
    if int(j) >=90:
        a += 1
    elif int(j)>=80:
        b += 1
    elif int(j)>=70:
        c += 1
    elif int(j)>=60:
        d += 1
    else:
        e += 1
print("这十名学生中得优的人数是{}人,得良的人数是{}人,得中的人数是{}人,得及格的人数是{}人,得不及格的人数是{}人".format(a,b,c,d,e))