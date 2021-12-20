f = open('temp.txt',encoding='utf-8')
line1 = f.readline().rsplit()
line1 = [ int(x) for x in line1 ]
# print(max(line1))
line2 = f.readline().rsplit()
line2 = [ int(x) for x in line2 ]
L3 =[]
for i in range(len(line1)):
    L3.append(int((line1[i]+line2[i])/2))
sum =0
k=0
for i in range(len(L3)):
    sum=sum+L3[i]
    if L3[i]>=10:
        k+=1
    else:
        k=0
avg=int(sum/len(L3))
print("本周平均气温为：",avg)
if k>=5:
    print("以入春")
else:
    print("未入春")
f.close()