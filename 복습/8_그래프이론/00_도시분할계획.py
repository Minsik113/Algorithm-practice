'''
1. 크루스칼이용해서 전체 도시연결
2. 가장긴 길을 기점으로 두 개의 도시로 나눔
-> 가장 긴 cost 삭제
3. 나머지 길들 다 더해라.

# 도시연결. 사이클 확인
'''
from collections import deque
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)
edges = []

# 대표 초기화
for i in range(1, n+1):
    parent[i] = i

# 길 오름차순 정렬
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))
edges.sort()

max_value = 0
result = 0

for edge in edges:
    cost, a, b = edge
    # 사이클인지 확인
    if find_parent(parent, a) != find_parent(parent, b): 
        union_parent(parent, a, b)
        max_value = max(max_value, cost)
        result += cost
print(result-max_value)


