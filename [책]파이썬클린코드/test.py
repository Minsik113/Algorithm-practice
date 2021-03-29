a = [1,2,3,4,5,6,7,8,9]
b = a[::]


print(id(a))
print(id(b))
b = a
print(id(a))
print(id(b))

print(a[:3])
interval = slice(None,3,1)
print(a[interval])