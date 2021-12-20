
def output_avg(L):
    sum1,sum2=0,0
    for line in L:
        L1 = line
        sum1 += int(L1[1])
        sum2 += int(L1[2])
    count = len(L)
    avg1 = round(sum1/count,1)
    avg2 = round(sum2/count,1)
    print("这个班数学平均成绩为：%4.1f"%avg1)
    print("这个班语文平均成绩为：%4.1f"%avg2)
 
def output_notpass(L):
    print("两门成绩均不及格的学生学号、数学和语文成绩为：")
    for line in L:
        L1 = line
        if int(L1[1])<60 and int(L1[2])<60:
            print(line)
 
def output_good(L):
    print("两门课平均分在90以上的学生学号、数学和语文成绩为：")
    for line in L:
        L1 = line
        f_score = round((int(L1[1])+int(L1[2]))/2)
        if f_score>=90:
            print(line)
 
f = open("class_score.txt")
L = f.readlines()
del L[0]
output_avg(L)
output_notpass(L)
output_good(L)
