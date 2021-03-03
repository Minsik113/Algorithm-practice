a = [1,2,3]
b = [1,2,3,4]
if a == b[:len(a)]:
    print('w')

print(a)
print(b[:len(a)])