'''
트리의 루트를 1이라고 정했을 때,
각 노드의 부모를 구해라

'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

# 1. 맵정보
graph = [[] for _ in range(n+1)] # 1~n
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1부터 쭉내려가면된다..
visited = [0] * (n+1) # i의 부모를 저장
def bfs(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for i in graph[now]:
            # 안본애라면
            if not visited[i]:
                visited[i] = now
                q.append(i)
bfs(1)
# for i in range(2, n+1):
#     print(visited[i])
for i in visited[2:]:
    print(i)