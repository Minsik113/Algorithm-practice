'''
bfs 연결리스트개수세기
-> 0,0 -> n-1,m-1 까지 연결리스트개수찾기
'''
from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input())) for i in range(n)]
answer = 0
dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    array[i][j] = 2 # 방문함
    
    while q:
        v = q.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if array[nx][ny] == 0:
                array[nx][ny] = 2
                q.append((nx,ny))
def dfs(i,j):
    array[i][j] = 2
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= m: # 4,5라면 0~3행 0~4열
            continue
        if array[nx][ny] == 0:
            dfs(nx,ny)

# def dfs(v): # 이론으론 stack이용한다고 하는데 실제로 코딩하면 재귀로 구현가능
#     print(v, end=' ')
#     visited[v] = True
#     for e in adj[v]:
#         if not (visited[e]): # 방문안했다면
#             dfs(e)

for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            # bfs(i,j)
            dfs(i,j)
            answer += 1
print(answer)
