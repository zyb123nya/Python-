import re
words=input("Input the words:")
l=re.split('[\. ]+',words)  #使用空格分隔词语，得到各个单词
print(l)
i=0
for i in l:
    print('')
