# List = [23, 65, 19, 90]
# print(List)
# pos1, pos2 = 1,3
# List[pos1-1],List[pos2-1]=List[pos2-1],List[pos1-1]
# print(List)

# def swap(lis):
#     p1,p2
#     lis[p1-1],lis[p2-1]=lis[p2-1],lis[p1-1]
#     return lis
# lis=[23,65,19,90]
# p1,p2=1,3
# print(swap(lis))

def sw(lis,p1,p2):
    temp=lis[p1]
    lis[p1]=lis[p2]
    lis[p2]=temp
    return lis
lis=[23,65,19,90]
p1,p2=1,3
print(sw(lis,p1-1,p2-1))

