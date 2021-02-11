'''
# 1/27
# 문제 난이도: Silver 2
# 문제 유형: DFS, BFS
# 추천 풀이 시간: 30분
'''
'''
이 문제에서는 '정점 번호가 작은 것'을 먼저 방문한다.
DFS, BFS 모두 O(N+M)이다.
★★★★이런 문제를 매우 빠르게 풀 수 있도록 숙달해야한다.★★★★
큐 구현을 위해 collections 라이브러리의 deque를 사용한다.
'''
from collections import deque

def dfs(v): # 이론으론 stack이용한다고 하는데 실제로 코딩하면 재귀로 구현가능
    print(v, end=' ')
    visited[v] = True
    for e in adj[v]:
        if not (visited[e]): # 방문안했다면
            dfs(e)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not (visited[v]):
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)


n, m, v = map(int, input().split())
adj = [ [] for i in range(n+1)] # 모든 정점에 대해 연결리스트

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# 작은 수부터 탐색하기 위하여
for e in adj:
    e.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
