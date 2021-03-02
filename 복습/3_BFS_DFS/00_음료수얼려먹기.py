'''
bfs 연결리스트개수세기
-> 0,0 -> n-1,m-1 까지 연결리스트개수찾기
'''

##########################################
##########################################
# 다시 품
from collections import deque

n, m = map(int, input().split())
visited = [[False]*m for i in range(n)]
# 맵 정보 입력받음
array = [list(map(int, input())) for i in range(n)]

def bfs(array, i, j, visited):
    visited[i][j] = True
    q = deque()
    q.append((i,j))
    dx = [-1,1,0,0] # 상하좌우
    dy = [0,0,-1,1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 0이면서 방문안한애라면 체크한다.
            if array[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
def dfs(i,j):
    if i < 0 or j < 0 or i >= n or j >= m:
        return False
    if array[i][j] == 0:
        array[i][j] = 2
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i,j+1)
        return True
    return False
# 연결관계 개수 찾기
count = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 0 and not visited[i][j]: # 1이면서 안가본곳이면 찾아라
            # bfs(array, i, j, visited) # array, (시작좌표), visited
            # count += 1
            if dfs(i,j):
                count += 1
print(count)
##########################################
##########################################
# 
# from collections import deque

# n, m = map(int, input().split())
# array = [list(map(int, input())) for i in range(n)]
# answer = 0
# dx = [-1,1,0,0] # 상하좌우
# dy = [0,0,-1,1]

# def bfs(i,j):
#     q = deque()
#     q.append((i,j))
#     array[i][j] = 2 # 방문함
    
#     while q:
#         v = q.popleft()
#         for i in range(4):
#             nx = v[0] + dx[i]
#             ny = v[1] + dy[i]
            
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if array[nx][ny] == 0:
#                 array[nx][ny] = 2
#                 q.append((nx,ny))
# def dfs(i,j):
#     array[i][j] = 2
#     for k in range(4):
#         nx = i + dx[k]
#         ny = j + dy[k]
#         if nx < 0 or ny < 0 or nx >= n or ny >= m: # 4,5라면 0~3행 0~4열
#             continue
#         if array[nx][ny] == 0:
#             dfs(nx,ny)

# # def dfs(v): # 이론으론 stack이용한다고 하는데 실제로 코딩하면 재귀로 구현가능
# #     print(v, end=' ')
# #     visited[v] = True
# #     for e in adj[v]:
# #         if not (visited[e]): # 방문안했다면
# #             dfs(e)

# for i in range(n):
#     for j in range(m):
#         if array[i][j] == 0:
#             # bfs(i,j)
#             dfs(i,j)
#             answer += 1
# print(answer)
