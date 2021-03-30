# ##########################################
# ##########################################
# # heapq로 count값 가져가면서 풀기
# import heapq

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs():
#     q = []
#     visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
#     heapq.heappush(q, (1,0,0,0)) # 거리, x,y, 벽
#     visited[0][0][0] = 1
    
#     while q:
#         count, x, y, wall = heapq.heappop(q)
#         if x == n-1 and y == m-1:
#             return count
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             # 지나갈 수 있는 곳
#             if visited[nx][ny][wall] == 0:
#                 # 길이면 가면됨
#                 if array[nx][ny] == 0:
#                     visited[nx][ny][wall] = 1
#                     heapq.heappush(q, (count+1, nx, ny, wall))
#                 # 벽이면서, 부술 수 있다면
#                 if array[nx][ny] == 1 and wall == 0:
#                     visited[nx][ny][1] = 1
#                     heapq.heappush(q, (count+1, nx, ny, 1))
#     for i in range(n):
#         for j in range(m):
#             print(visited[i][j][0], end=' ')
#         print()
#     print()
#     for i in range(n):
#         for j in range(m):
#             print(visited[i][j][1], end=' ')
#         print()
#     return -1

# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     array = [list(map(int, input())) for _ in range(n)]
#     result = bfs()
#     print(result)
# ##########################################
# ##########################################
# # 배열 크기를 바꾸면서 감
# # '''
# # 벽을 뚫었을때랑
# # 벽 안뚫고갈때
# # ->3차원리스트만들어라 
# # ck[x][y][0] = 벽안뚫고감
# # ck[x][y][1] = 벽뚫고감
# # x,y좌표에는 여기까지 오는데 걸리는 거리.
# # '''

# # from collections import deque

# # dx = [-1,1,0,0]
# # dy = [0,0,-1,1]

# # def bfs():
# #     q = deque()
# #     q.append([0,0,0]) # (0,0), 벽안뚫음
# #     check = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# #     check[0][0][0] = 1
# #     while q:
# #         x, y, wall = q.popleft()
# #         if x == n-1 and y == m-1:
# #             return check[x][y][wall]
# #         for i in range(4):
# #             nx = x + dx[i]
# #             ny = y + dy[i]
# #             if nx < 0 or ny < 0 or nx >= n or ny >= m:
# #                 continue
# #             # 안본곳 -> 갈 수 있다면 -> +1 해준다
# #             if check[nx][ny][wall] == 0:
# #                 if array[nx][ny] == 0:
# #                     check[nx][ny][wall] = check[x][y][wall] + 1
# #                     q.append([nx, ny, wall])
# #                 # 벽으로 막혀있다면? 부술수있는지 본다
# #                 if array[nx][ny] == 1 and wall == 0:
# #                     check[nx][ny][1] = check[x][y][0] + 1
# #                     q.append([nx, ny, 1])
# #     return -1

# # n, m = map(int, input().split())
# # array = [list(map(int, input())) for _ in range(n)]

# # print(bfs())

