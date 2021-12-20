def add_dic(dic):
    while True:
        word = input("请输入英文单词：")
        if len(word)==0:
            break
        meaning=input("请输入中文翻译：")
        dic[word]=meaning
        print("已添加")
    return
def search(dic):
    while True:
        word = input("请输入查询英文单词：")
        if len(word)==0:
            break
        if word in dic:
            print("%s的中文是%s"%(word,dic[word]))
        else:
            print("字典库暂无")
    return
worddic = dict()
while True:
    print("1:输入 2：查找 3：退出")
    c=input()
    if c =='1':
        add_dic(worddic)
    elif c=='2':
        search(worddic)
    elif c=='3':
        break