# l=[3,2,4]
# count=1
# for i in l:
#     count=count*i
# print(count)



# def mul(l):
#     count=1
#     for i in l:
#         count=count* i
#     return count
# l1=[1,2,3]
# print(mul(l1))
# l2=[7,2,2,2]
# print(mul(l2))


# using traversal by index

def mul(list):
    r=1
    for i in range(0,len(list)):
        r=r*list[i]
    return r
l=[1,2,45]
print(mul(l))


