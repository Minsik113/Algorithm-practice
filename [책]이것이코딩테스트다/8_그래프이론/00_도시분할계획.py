'''
2개로 분리한다.
제일긴 거리없애면 될듯.

1. MSP를 이용해 최소신장트리이용.
2. 토탈거리 - 제일긴edge길이 = 답
'''
from collections import deque 
import sys
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

# 1. 부모테이블 선언 및 초기화(cycle체크하기 위해)
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# 비용 입력받는다
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# MSP (크루스칼)수행
edges.sort()

total = 0
max_value = 0
for edge in edges: # 제일 짧은 거리를 계쏙뽑으면서 비교 
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += cost
        max_value = max(max_value, cost)

print(total - max_value)
