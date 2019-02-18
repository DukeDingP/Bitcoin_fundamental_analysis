b=[1,2,3,4,5]
a=b
del a[0:1]
print(a)
print(b)

#可以看到数组 a b 同时变化

b=[1,2,3,4,5]
a=b
a.pop(0)
print(a)
print(b)

#pop 和 del 同样是这样
a=[]
b=[1,2,3,4,5]
for i in range(len(b)):
    a.append(b[i])
del a[0:1]
print(a)
print(b)

#可见通过构造函数可以避免同时相减