'''
bfs를 이용해서 칸을 세자
1,1 -> n,m

나는 0,0 -> n-1, m-1 이렇게 할 것임.

'''
# 3/29 - bfs
from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False] * (m) for _ in range(n)]
def bfs(array, x, y):
    q = deque()
    q.append((1, x, y))
    visited[x][y] = True
    while q:
        cost, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == n-1 and ny == m-1:
                return cost + 1
            # 범위벗어남 or 벽(0) or 이미본곳
            if nx < 0 or ny < 0 or nx >= n or ny >= m or array[nx][ny] == 0 or visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            q.append((cost+1, nx, ny))
            
result = bfs(array, 0, 0)
print(result)