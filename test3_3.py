#O(N)
f=open('score2.txt')
a=f.readlines()
L2=[]
L3=[]
for line in a:
    line=line.strip()
    L1=line.split()
    L2.append(L1[0])
    L3.append(L1[1])
f.close()
maxscore=L3[0]
maxindex=0
minscore=L3[0]
minindex=0
for i in range(1,len(L3)):
    if L3[i]>maxscore:
        maxscore=L3[i]
        maxindex=i
    if L3[i]<minscore:
        minscore=L3[i]
        minindex=i
print("最高分为%s,学号为%s"%(str(maxscore),str(L2[maxindex])))
print("最低分为%s,学号为%s"%(str(minscore),str(L2[minindex])))