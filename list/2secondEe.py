def sec(list):
    list[1],list[-3]=list[-3],list[1]
    return list
g=[10,20,30,40,4]
print(g)
print(sec(g))

