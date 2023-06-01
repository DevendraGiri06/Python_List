# def swaplist(newlist):
#     newlist[0],newlist[-2]=newlist[-2],newlist[0]
#     return newlist

# newlist=eval(input('enter the list'))
# print(newlist)
# print(swaplist(newlist))


# r=[1,2,3,4]
# print(r[0])
# print(r[-4])

# swap using tuple 
def tuswap(lis):
    get = lis[0],lis[-1]
    lis[-1],lis[0]=get

    return lis
lisy=[1,2,34,48]
print(lisy)
print(tuswap(lisy))
