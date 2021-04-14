'''
땅의 개수 세라.
answer: 섬의 개수는 ?
'''
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # 3. 2번을 간결하게 풀이
        def dfs(i, j) -> None:
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                    return
            
            grid[i][j] = 0 # 육지->물 로 바꿈.
            
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
    
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
    
        # 2. dfs
#         def dfs(i, j) -> None:
#             if i < 0 or i >= len(grid) or \
#                 j < 0 or j >= len(grid[0]) or \
#                 grid[i][j] != '1':
#                     return
            
#             grid[i][j] = 0 # 육지->물 로 바꿈.
#             for k in range(4):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 dfs(nx, ny)
            
#         dx = [-1, 1, 0, 0]
#         dy = [0, 0, -1, 1]
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     dfs(i, j)
#                     count += 1
#         return count
        
        # 1. bfs로 구현
#         row, col = len(grid), len(grid[0])
#         visited = [[False] * col for _ in range(row)]
#         answer = 0
#         dx = [-1, 1, 0, 0] # 상 하 좌우
#         dy = [0, 0, -1, 1]
#         def bfs(visited, i, j) -> None:
#             q = deque()
#             q.append((i, j))
#             visited[i][j] = True
#             while q:
#                 x, y = q.popleft()
#                 for k in range(4):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if nx < 0 or ny < 0 or nx >= row or ny >= col:
#                         continue
#                     if grid[nx][ny] == "1" and not visited[nx][ny]:
#                         visited[nx][ny] = True
#                         q.append((nx, ny))
        
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == "1" and not visited[i][j]:
#                     bfs(visited, i, j)
#                     answer += 1
        
#         return answer