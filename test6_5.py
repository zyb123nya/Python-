str = input('input some string:')

for i in set(list(str)):
    print("%s,%d" % (i, str.count(i)))