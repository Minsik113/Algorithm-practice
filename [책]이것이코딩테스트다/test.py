'''
터널 연결할때 비용

MST문제
'''
import sys, heapq
from collections import deque
input = sys.stdin.readline

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

n = int(input())
x = []
y = []
z = []
for i in range(n):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))
x.sort()
y.sort()
z.sort()

edges = []
for i in range(1, n):
    heapq.heappush(edges, (abs(x[i-1][0] - x[i][0]), x[i-1][1], x[i][1]))
    heapq.heappush(edges, (abs(y[i-1][0] - y[i][0]), y[i-1][1], y[i][1]))
    heapq.heappush(edges, (abs(z[i-1][0] - z[i][0]), z[i-1][1], z[i][1]))

parent = [0] * (n+1)
for i in range(n):
    parent[i] = i

result = 0
while edges:
    dist, a, b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += dist
print(result)
