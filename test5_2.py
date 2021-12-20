from numpy.lib.function_base import average
import pandas as pd
def function1(filename):
    data = pd.read_table(filename,header=None)
    index = data[0]
    data1 = data[1]
    data2 = data[2]
    avg_data = (data[1]+data[2])/2
    x = list(index)
    y = list(avg_data)
    stu =zip(list(index),list(avg_data))
    # print(dict(stu))
    print("每个学生的平均分")
    for x in stu:
        print (x)
function1("score3.txt")
def calAvg():
    data = pd.read_table("score3.txt",header=None)
    data1 = data[1]
    data2 = data[2]
    print("专业课1的班级平均分为%s"%average(data1))
    print("专业课2的班级平均分为%s"%average(data2))
calAvg()