'''
2의 위치를 찾는다.

'''

n, m = map(int, input().split()) # n높이 m너비
array = []
for i in range(n):
    array.append(list(map(int,input().split())))
print(array)