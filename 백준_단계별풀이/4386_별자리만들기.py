##########################################
##########################################
4/1 - 첫풀이
'''
connected acyclic graph 이어야 최소비용이나옴
mst

'''
import math, heapq, sys
input = sys.stdin.readline

# a, b의 거리를 구해라
def distance(a, b):
    return math.sqrt((stars[a][0] - stars[b][0])**2 + (stars[a][1] - stars[b][1])**2)

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

# 1. 별자리들의 위치를 저장한다
stars = [[] for _ in range(n+1)]
for i in range(1, n+1):
    x, y = map(float, input().split())
    stars[i].append(x)
    stars[i].append(y)

# 2. 각 별들의 거리를 구한다
edges = []
for i in range(1, n+1):
    for j in range(i+1, n+1):
        # print(i, j, distance(i,j))
        heapq.heappush(edges, (distance(i,j),i,j))

# 3. 부모 선언 및 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

result = 0
while edges:
    weight, a, b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += weight

print('%.2f' % result)
