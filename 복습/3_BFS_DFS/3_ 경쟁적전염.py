'''
1. S초후에 (x,y) 에 존재하는 바이러스 출력하라
2. 없으면 0출력

-> 바이러스 종류 오름차순리스트로 정렬.
각 바이러스마다 bfs한번씩한다.
'''
'''
1. bfs로 바이러스 증식.
-> 번호가 낮은것부터 증식해야함. heapq?
2. s초가 지난 후 (x,y)에있는 바이러스 번호찾기
3. (x,y)가 오염되지 않았다면 0 출력
'''
##########################################
##########################################
# 3/2
import heapq
from collections import deque

n, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
s, fx, fy = map(int,input().split()) 

h = []
# 시작위치찾는데 200*200 = 4만
max_virus = 0
for i in range(n):
    for j in range(n):
        if array[i][j] != 0:
            h.append((array[i][j],i,j,0))
            max_virus = max(max_virus, array[i][j])
h = sorted(h, key=lambda x:x[0]) # virus 기준으로 오름차순정렬
# 정렬된 리스트 -> deque()로
# qq = deque(h) 하면 바로됨.
qq = deque()
for i in h:
    qq.append(i)

def bfs(array, qq):
    global max_virus, result
    while qq:
        virus, x, y, time = qq.popleft()
        # 바이러스 퍼트리기 전에 확인한다.
        if time == s:
            return
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if array[nx][ny] == 0:
                array[nx][ny] = virus
                qq.append((virus,nx,ny,time+1))
                
# 바이러스 순서대로 bfs진행
result = 0
bfs(array, qq)
# print(array)
print(array[fx-1][fy-1])
# ##########################################
# ##########################################
# # 
# from collections import deque 

# n, k = map(int, input().split()) # nxn, k개의바이러스
# array = [] # 1~n
# virus_type = [0] * 1001 # 1~1000
# save_pos = []
# for i in range(n):
#     array.append(list(map(int, input().split())))
# time, x, y = map(int, input().split())

# for i in range(n):
#     for j in range(n):
#         if array[i][j] != 0:
#             save_pos.append((i,j,array[i][j],0)) # (x,y,바이러스번호,초)

# # 바이러스 번호로 오름차순정렬
# save_pos.sort(key=lambda x:x[2]) 

# # 바이러스 번호 순으로 bfs시작
# dx = [-1, 1, 0, 0] # 상하좌우
# dy = [0, 0, -1, 1]
# # 리스트 -> deque로 변환
# save_pos = deque(save_pos)

# while save_pos:
#     now = save_pos.popleft()
#     row, col, virus, t = now[0], now[1], now[2], now[3] # 좌표,virus번호
#     if t == time: # 다봤으므로
#         break
#     # print(row,col,virus)
#     for i in range(4):
#         nx = row + dx[i]
#         ny = col + dy[i]
#         if nx < 0 or ny < 0 or nx >= n or ny >= n:
#             continue
#         # 옮길 수 있으면 옮기자
#         if array[nx][ny] == 0:
#             array[nx][ny] = virus
#             save_pos.append((nx,ny,virus,t+1))

# # print(array)
# print(array[x-1][y-1])
