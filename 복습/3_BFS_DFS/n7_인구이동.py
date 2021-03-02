# '''
# 1/ 상하좌우빼보고 l~r범위에 있는거 visited로체크한다.
# 2/ vistied체크됐으면 모든수 합한다(sum_value)
# 3/ vistied체크된 수 구한다.(count)
# 4/ visited체크된 곳은 sum_value/count 로 바꿈
# 5. 1,2,3,4반복
# '''
# from collections import deque

# n, l, r = map(int, input().split())
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(i, j):
#     q = deque()
#     q.append((i,j))
#     while q:
#         x, y = q.popleft()
#         visited[x][y] -= 1
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             if visited[nx][ny] > 0:
#                 q.

# # 거리 비교할 좌표구하자.
# result = 0
# while True:
#     print(array)
#     visited = [[0] * n for _ in range(n)]
#     check = False # 한번도 바꿀게 없는지 체크
#     for i in range(n):
#         for j in range(n):
#             for x in range(4):
#                 nx = i + dx[x]
#                 ny = j + dy[x]
#                 if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                     continue
#                 # 범위안에 있고 둘다 안본애라면
#                 if abs(array[i][j] - array[nx][ny]) >= l and abs(array[i][j] - array[nx][ny]) <= r:
#                     if visited[i][j] == 0 or visited[nx][ny] == 0:
#                         visited[i][j] += 1
#                         visited[nx][ny] += 1
#                         check = True
#     # 바꿀게 없으면 나옴
#     if not check:
#         break
#     # 연합 인구 합, 총 연합 수
#     # 여기에서 bfs해야함
#     for i in range(n):
#         for j in range(n):
#             if visited[i][j] > 0:
#                 bfs(i,j)

#     # 값 바꿔준다
#     x = int(total/low)
#     for i in range(n):
#         for j in range(n):
#             if visited[i][j] == 1:
#                 array[i][j] = x
#     result += 1

# print(result)