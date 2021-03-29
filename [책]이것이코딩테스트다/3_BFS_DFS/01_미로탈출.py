'''
(1,1) -> (N,M) 
1. 1로만다닌다.
2-1. 갔다가 아니면 돌아와야함. -> 이건 dfs방식
2-2. bfs로 계속 계층마다 다 찾는다.
3. 방문횟수를 가지고간다.

'''
##########################################
##########################################
# array값 바꾸면서 간다.
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

##########################################
##########################################
# count를 가지고가자.
'''
(1,1) -> (n,m)
1 = 길
0 = 괴물
'''
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int,input())) for i in range(n)]
# bfs시작
def bfs(graph,i,j):
    level_ = 1
    q = deque()
    q.append((level_,i,j))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    graph[i][j] = 2
    while q:
        level, x, y = q.popleft()
        print(level,'일때',x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == n-1 and ny == m-1: # 정답에 왔다면
                return level+1
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                q.append((level+1, nx, ny))

result = bfs(graph,0,0)
print(result)
