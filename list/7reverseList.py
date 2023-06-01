# using slicing

# list = [1, 2, 3, 4, 5]
# print(list[::-1])

# reversing list using insert function 

# lst = [1,2,45,6,7,8]
# lst2=[]
# for i in lst:
#     lst2.insert(0,i)
# print(lst2)

# reversinglist using a two pointer approach

def reverse_list(arr):
    left=0
    right=len(arr)-1
    while(left<right):
        temp=arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left +=1
        right -=1
    return arr
arr = [1,2,4,6,7,89,78]
print(reverse_list(arr))