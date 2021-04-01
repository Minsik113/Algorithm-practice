'''
mst구해라

union-find로 사이클 체크하면서 해야함

'''
import heapq, sys
input = sys.stdin.readline

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

v, e = map(int, input().split())

# 1. 부모 선언 및 초기화
parent = [0] * (v+1)
for i in range(v+1):
    parent[i] = i

# 2. 간선정보
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(edges, (c, a, b))

# 3. MST START
result = 0 
total = 0
while edges:
    cost, a, b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        total += 1
        if total == v: # v개 모두 다보면 그만본다
            break
print(result)