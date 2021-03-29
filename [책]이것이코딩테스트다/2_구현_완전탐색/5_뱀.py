##########################################
##########################################
# 동빈나풀이
'''
1. 매시점 뱀이 존재하는 위치를 항상 2차원 리스트에 기록
'''
# n = int(input())
# k = int(input())
# data = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
# info = [] # 방향 회전 정보

# # 맵 정보(사과는 1로 표기)
# for _ in range(k):
#     a, b = map(int, input().split())
#     data[a][b] = 1
# # 방향 회전 정보 입력
# l = int(input())
# for _ in range(l):
#     x, c = map(int, input().split())
#     info.append((int(x),c))
# # 처음에 오른쪽 보고있으므로
# dx = [0, 1, 0, -1] # 동남서북
# dy = [1, 0, -1, 0]

# def turn(direction, c):
#     if c == 'L':
#         direction = (direction - 1) % 4
#     else:
#         direction = (direction + 1) % 4
#     return direction

# def simulate():
#     x, y = 1, 1 # 시작위치
#     data[x][y] = 2 # 뱀위치
#     direction = 0 # 동쪽보고있음
#     time = 0 # 시작부터 걸리는 초
#     index = 0 # 다음에 회전할 정보
#     q = [(x,y)] # 뱀이 차지하는 위치 정보(꼬리가 앞쪽)
#     while True:
#         nx = x + dx[direction]
#         ny = y + dy[direction]
        
#         # 맵 범위 안에 있고, 뱀이 아닐 때,
#         if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
#             # 사과가 없다면 이동 후 꼬리 제거
#             if data[nx][ny] == 0:
#                 data[nx][ny] = 2
#                 q.append((nx,ny))
#                 px, py = q.pop()
#                 data[px][py] = 0
#             # 사과가 있다면 이동 후 꼬리 그대로 
#             if data[nx][ny] == 1:
#                 data[nx][ny] = 2
#                 q.append((nx,ny))
#         # 맵 or 벽에 부딪혔을 때
#         else:
#             time += 1
#             break
        
#         x, y = nx, ny # 다음 위치로 머리 이동
#         time += 1
#         if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
#             direction = turn(direction, info[index][1])
#             index += 1
#     return time
# print(simulate())

##########################################
##########################################
# 내풀이
'''
1. deque()를 활용해서 뱀의 위치 나타냄.
->사과 먹었으면 q.append((nowx,nowy))
->사과 안먹었으면 q.popleft() q.append(nowx,nowy)

2. 이동하다가 범위벗어나거나, q에 있는곳을 만나면 끝냄
-> 다음칸 먼저 가보고 꼬리면 죽음. 빈칸이면 꼬리축소
'''
# from collections import deque

# n = int(input())
# k = int(input()) # 사과 개수
# # 사과위치
# apples = dict()
# for _ in range(k):
#     x, y = map(int, input().split())
#     apples[(x,y)] = 1
# # 뱀의 방향정보
# m = int(input())
# moves = []
# for _ in range(m):
#     x, direct = input().split()
#     moves.append((int(x),direct))

# # 1. 맵 만들자
# array = [[0]*(n+1) for i in range(n+1)] # (1,1)~(n,n)

# # 2. 이동해보자
# dx = [-1,0,1,0] # 북동남서
# dy = [0,1,0,-1]
# x, y = 1, 1

# # 방향전환
# def check(chr_direct, now):
#     if chr_direct == 'D': # 오른쪽으로
#         now += 1
#         if now > 3:
#             now = 0
#     else: # 왼쪽
#         now -= 1
#         if now < 0:
#             now = 3
#     return now

# q = deque()
# result = 0
# nx, ny = 1, 1
# now = 1 # '동쪽으로' index
# q.append((x,y))
# while True:
#     for move in moves:
#         time, chr_direct = move

#         # time초 될 때까지 일단 방향대로감
#         while result < time:
#             nx = nx + dx[now]
#             ny = ny + dy[now]
#             result += 1 # 시간증가
#             # print('현재볼곳',nx,ny)
#             # 1번. 다음칸 = 사과 -> 길이 늘어남
#             if (nx,ny) in apples and apples[(nx,ny)]==1:
#                 apples[(nx,ny)] -= 1
#             else: # 2번. 사과가아니라면
#                 # a) 다음칸 = 벽or뱀
#                 if nx < 1 or nx > n or ny < 1 or ny > n or (nx,ny) in q: 
#                     # print('중간에끝남',result)
#                     print(result)
#                     exit()
#                 else: # b) 다음칸 = 땅 -> 길이축소
#                     q.popleft()
#             q.append((nx,ny))
#             # print('지금',nx,ny,q)
#         # 아무사고없이 쭉 왔다면 time에서 방향전환 해야함
#         now = check(chr_direct, now)

#     # 시간 다 봤는데도 사고가 안났다면 지금 방향으로 벽or뱀 만날때까지 쭉간다.
#     # now는 방향
#     while True:
#         nx = nx + dx[now]
#         ny = ny + dy[now]
#         result += 1
#         if nx < 1 or nx > n or ny < 1 or ny > n or (nx,ny) in q: 
#             break
#     break
# print(result)
