# def minA(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# a,b=250,-1000
# print(minA(a,b))

# usin max method 
# a,b=-4,10
# v=max(a,b)
# print(v)

#  using ternary operater 
# a,b=45,50
# x=a if a>b else b
# print(x)
# print(a if a>b else b)

# using lambda 
a=10
b=6
g=lambda a,b:a if a>=b else b
# print(f'{g(a,b)}')

print(g(a,b))


# using list comprhensenn
i,j=45,74
l=([i if i>j else j])
print(l)

# using sort ()method
h,k=415,78
v=[h,k]
v.sort()
print(v[-1])

