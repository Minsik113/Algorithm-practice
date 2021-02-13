# 조건 양옆집의 색이 달라야함
# 

# R G B
import time
start_time = time.time()
##########################################
##########################################
# # # # # # # # 코 드 넣 어 # # # # # # # #
'''
(1,1) -> (N,M) 
1. 1로만다닌다.
2-1. 갔다가 아니면 돌아와야함. -> 이건 dfs방식
2-2. bfs로 계속 계층마다 다 찾는다.
3. 방문횟수를 가지고간다.

'''
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
visited = [[False]*(m) for i in range(n)]
for i in range(n):
    save = list(map(int, input()))
    array.append(save)
    for j in range(len(save)):
        if save[j] == 0:
            visited[i][j] = True

count = 1 
dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

def bfs(x,y,count):
    q = deque()
    # q.append((x-1,y-1,count)) # (1,1)이 들어왔지만 우리는 0,0부터 n-1,m-1까지 볼것이므로
    q.append((x,y,count))
    visited[x][y] = True
    while q:
        v = q.popleft()
        zx, zy, level = v[0], v[1], v[2]
        # print(v,'=',zx,zy,level)
        for k in range(4):
            nx = zx + dx[k]
            ny = zy + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if array[nx][ny] == 1:
                if nx == n-1 and ny == m-1: # 정답찾으면 level출력
                    print(level+1)
                    return
                q.append((nx,ny,level+1))
                    
# bfs(1,1,count)
bfs(0,0,count)

##########################################
##########################################
end_time = time.time()
print(end_time-start_time)