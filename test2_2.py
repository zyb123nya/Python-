f = open('temp.txt',encoding='utf-8')
line1 = f.readline().rsplit()
line1 = [ int(x) for x in line1 ]
# print(max(line1))
print("最高气温为%d"%max(line1))
line2 = f.readline().rsplit()
line2 = [ int(y) for y in line2 ]
print("最低气温为%d"%min(line2))
f.close()