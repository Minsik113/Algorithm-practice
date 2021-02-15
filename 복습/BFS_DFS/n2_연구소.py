'''
2의 위치를 찾는다.
n, m 3~8까지 -> 맵의 2마다 퍼질 수 있는 

'''

n, m = map(int, input().split()) # n높이 m너비
array = []
for i in range(n):
    array.append(list(map(int,input().split())))
print(array)