from test2_5 import L1


f = open('score1.txt',encoding='utf-8')
a=f.readline()
line =(f.readline()).strip()
f2=open("score2.txt","w")
f2.write("学号  平均成绩 \n")
L2=[0,0,0,0,0]
count=0
sum=0
while (len(line)!=0):
    L1=line.split()
    f2.write(L1[0]+" ")
    f_score=int(int(L1[1])*0.4+int(L1[2])*0.6)
    if 90<f_score<=100:
        L2[0]+=1
    elif f_score>=80:
        L2[1]+=1
    elif f_score>=70:
        L2[2]+=1
    elif f_score>=60:
        L2[3]+=1
    else:
        L2[4]+=1
    count+=1
    sum+=f_score
    f2.write(str(f_score)+'\n')
    line=(f.readline()).strip()
    
f.close()
f2.close()
avg_score=int(sum/count)
print("总人数%d,90以上%d人,80-89%d人,70-79%d人,60-69%d人,60以下%d人,平均分为%d分"
%(count,L2[0],L2[1],L2[2],L2[3],L2[4],avg_score))