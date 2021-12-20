cost = 0.0325
count = 10000
year=0
while count <20000:
    year +=1
    count = count*(1+cost)
print("%s年以后会翻番"%year)