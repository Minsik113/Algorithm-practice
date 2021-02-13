'''
(1,1) -> (N,M) 
1. 1로만다닌다.
2-1. 갔다가 아니면 돌아와야함. -> 이건 dfs방식
2-2. bfs로 계속 계층마다 다 찾는다.
3. 방문횟수를 가지고간다.

'''
from collections import deque
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input())))

dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x, y  = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if array[nx][ny] == 0:
                continue
            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                q.append((nx,ny))
    return array[n-1][m-1]

print(bfs(0,0))
