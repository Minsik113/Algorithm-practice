'''
mst

'''
import sys, heapq, math
input = sys.stdin.readline

def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

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

# MAIN START
n, m = map(int, input().split())

# 1. 우주신들의 좌표
gods = [] # 0~n-1
for i in range(1, n+1):
    a, b = map(int, input().split())
    gods.append([a, b]) 

# 2. 부모 선언 및 초기화
parent = [0] * (n+1) # 1~ n
for i in range(1, n+1):
    parent[i] = i

# 3. 이미 연결된 우주신들
for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 우주신들의 거리를 보자 = 100만
edges = []
for i in range(n-1):
    for j in range(i+1, n):
        dif = distance(gods[i], gods[j])
        heapq.heappush(edges, (dif, i, j))

result = 0
while edges:
    cost, x, y = heapq.heappop(edges) # 0~n-1 까지니까 1~n으로 바꿔야함
    if find_parent(parent, x+1) != find_parent(parent, y+1):
        union_parent(parent, x+1, y+1)
        result += cost

print("%.2f" % result)