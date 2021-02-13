test = int(input())
array = []

for i in range(test):
    a, b = map(str, input().split())
    # a,b = input().split()
    array.append((a,int(b)))
array.sort(key=lambda x:x[1])

for i in array:
    print(i[0], end=' ')