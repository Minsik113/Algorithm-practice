'''
가장 먼 헛간 찾아라
1에서 제일먼 노드

-> bfs로 접근하면됨

'''
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

# 맵입력받음
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # a->b
    graph[b].append(a)

visited = [False] * (n+1)
count = [0] * (n+1)
def bfs(start, count, visited):
    q = deque()
    q.append((0, start))
    visited[start] = True
    count[start] = 0
    while q:
        dist, now = q.popleft()
        for v in graph[now]:
            if not visited[v]:
                q.append((dist+1, v))
                count[v] = dist+1
                visited[v] = True

bfs(1,count,visited)
number = 0
max_value = max(count)
same_number = count.count(max_value)
for i in range(1, n+1):
    if max_value == count[i]:
        number = i
        break
print(number, max_value, same_number)

