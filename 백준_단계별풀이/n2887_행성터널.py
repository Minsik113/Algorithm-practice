'''
a, b 두행성의 길이는
min(|xA-xB|, |yA-yB|, |zA-zB|) 임

mst

n = 10^5라서 O(NlogN) = 2천만.
'''
import sys, heapq
input = sys.stdin.readline

def distance(i, j):
    dif = min(abs(x[i]-x[j]), abs(y[i]-y[j]))
    dif = min(dif, abs(z[i]-z[j]))
    return dif

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

n = int(input())

# 1. 거리를 입력받자
x = []; y = []; z = []
for i in range(n):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))
x.sort()
y.sort()
z.sort()

# 2. 짧은애들순으로 heap에 넣자
edges = []
for i in range(n-1):
    heapq.heappush(edges, (abs(x[i+1][0]-x[i][0]), x[i+1][1], x[i][1] ))
    heapq.heappush(edges, (abs(y[i+1][0]-y[i][0]), y[i+1][1], y[i][1] ))
    heapq.heappush(edges, (abs(z[i+1][0]-z[i][0]), z[i+1][1], z[i][1] ))
    
# 부모 선언 및 초기화
parent = [0] * (n)
for i in range(n):
    parent[i] = i

result = 0
while edges:
    cost, a, b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)


# '''
# a, b 두행성의 길이는
# min(|xA-xB|, |yA-yB|, |zA-zB|) 임

# mst

# n = 10^5라서 O(NlogN) = 2천만.
# '''
# import sys, heapq
# input = sys.stdin.readline

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# n = int(input())

# # 1. 거리를 입력받자
# planets = [] # O(10만)
# for _ in range(n):
#     data = list(map(int, input().split()))
#     planets.append(data)

# # 2. 짧은애들순으로 heap에 넣자
# x = []
# y = []
# z = []
# for i in range(n-1):
#     for j in range(i+1, n):
#         x.append((abs(planets[i][0] - planets[j][0]), i, j)
#         y.append((abs(planets[i][1] - planets[j][1]), i, j)
#         z.append((abs(planets[i][2] - planets[j][2]), i, j)
# x.sort(key=lambda x:x[0])
# y.sort(key=lambda x:x[0])
# z.sort(key=lambda x:x[0])

# # 부모 선언 및 초기화
# parent = [0] * (n)
# for i in range(n):
#     parent[i] = i

# result = 0
# while edges:
#     cost, a, b = heapq.heappop(edges)
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
# print(result)