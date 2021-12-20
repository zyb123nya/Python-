stud={"s1":45,"s2":78,"s3":40,"s4":96,"s5":65,"s6":90,"s7":78,"s8":99,"s9":60,"s10":87}
list1=list(stud.keys())
list2=list(stud.values())
for i in range(0,10):
    for j in range(0,9):
        if list2[j]>list2[j+1]:
            temp1=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp1
            temp2=list2[j]
            list2[j]=list2[j+1]
            list2[j+1]=temp2
print("成绩由低到高排列为：")
for i in range(0,10):
    print(list1[i],":",list2[i],";")