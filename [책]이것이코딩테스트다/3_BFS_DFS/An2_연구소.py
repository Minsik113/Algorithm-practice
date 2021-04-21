##########################################
##########################################
# 4/21 왜이리 느리지? 3월에푼게 더 빠름
# 1. combination으로 나오는거 다 뽑아놓고 bfs()호출하는게 
# 2. combination으로 결과 나올때마다 반복문쓰는거
# 왜 1번이 2번보다빠르지? ㄷㄷ
#
'''
시물레이션 문제
1. 벽세울수 있는 위치 찾음
2. 벽세운다
3. 조건찾아본다
4. 조건에 맞으면 값저장
4-1. 조건에 틀리면 벽 수거한다.

5. 1 2 3 4반복 후 값저장한 max값출력

'''
from itertools import combinations
from collections import deque
import copy
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

bar = []
virus = deque()
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            bar.append((i, j))
        elif array[i][j] == 2:
            virus.append((i, j))

result = 0
total = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
possible = []
for new_bar in list(combinations(bar, 3)):
    possible.append(new_bar)

while possible:
    v1, v2, v3 = possible.pop()
    # 벽설치
    array[v1[0]][v1[1]] = 1
    array[v2[0]][v2[1]] = 1
    array[v3[0]][v3[1]] = 1

    # 바이러스 퍼트린다.
    q = copy.deepcopy(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if array[nx][ny] == 0:
                array[nx][ny] = 3
                q.append((nx, ny))
    # 안전 영역 최대 크기
    total = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                total += 1
    result = max(result, total)
    # 원상복구
    for i in range(n):
        for j in range(m):
            if array[i][j] == 3:
                array[i][j] = 0
    array[v1[0]][v1[1]] = 0
    array[v2[0]][v2[1]] = 0
    array[v3[0]][v3[1]] = 0

print(result)

# '''
# 벽3개 설치한 모든 경우를 다 본다.

# '''
# 64C3하면 60^3 약22만번
# 3개 들어갈 수 있는 곳에 벽을 다 설치 
# '2' 퍼트리기
# 0의 개수세기
'''
모든경우의 벽 설치했을때 64C3이므로 약4만번
1. 벽 세우고 안전영역 수 계산
2. 벽 원상복구
3. 1,2반복
'''
##########################################
##########################################
# bfs, 완전탐색, Combinations 이용
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
array = [list(map(int, input().split())) for i in range(n)]

# 탐색
def bfs(array, x, y):
    q = deque()
    q.append((x,y))
    while q:
        v1, v2 = q.popleft()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = v1 + dx[i]
            ny = v2 + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if array[nx][ny] == 0: # 오염시킴
                array[nx][ny] = 3
                q.append((nx,ny))

# 설치할 수 있는 벽들 뽑아냄
pos = [] # 벽돌 설치 할 수 있는 좌표
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            pos.append((i,j))
possible = []
for i in combinations(pos,3):
    possible.append(list(i))

# 벽 설치 ㄱㄱ
max_value = 0
while possible: # 모든벽들 볼것이다.
    count = 0
    v1, v2, v3 = possible.pop()
    array[v1[0]][v1[1]] = 1
    array[v2[0]][v2[1]] = 1
    array[v3[0]][v3[1]] = 1
    # 오염 시킴
    for i in range(n):
        for j in range(m):
            if array[i][j] == 2:
                bfs(array, i, j)
    # 0의 개수 세자
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                count += 1
    max_value = max(max_value, count)
    # 원상복구
    for i in range(n):
        for j in range(m):
            if array[i][j] == 3:
                array[i][j] = 0
    array[v1[0]][v1[1]] = 0
    array[v2[0]][v2[1]] = 0
    array[v3[0]][v3[1]] = 0
print(max_value)
##########################################
##########################################
# dfs, 완전탐색, 
# n, m = map(int, input().split())
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))
# temp = [[0]*m for _ in range(n)] # 바이러스 증식시키고 원상복구시킬 맵

# dx = [-1, 1, 0, 0] # 상하좌우
# dy = [0, 0, -1, 1]
# result = 0

# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or ny < 0 or nx >= n or ny >= m:
#             continue
#         if temp[nx][ny] == 0:
#             temp[nx][ny] = 2
#             virus(nx,ny)

# def get_score():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#     return score
# # dfs이용해서 울타리짓고, 안전영역 개수 세기
# # import copy
# def dfs(count):
#     global result
#     if count == 3: # 안전지대 개수세자
#         # temp = copy.deepcopy(array)
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = array[i][j]
#         # 각 바이러스의 위치에서 전파
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i, j)
#         # 안전영역크기 계산
#         result = max(result, get_score())
#         return
#     for i in range(n):
#         for j in range(m):
#             if array[i][j] == 0:
#                 array[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 count -= 1
#                 array[i][j] = 0
    
# dfs(0)
# print(result)

# # n, m = map(int, input().split()) # n높이 m너비
# # array = [] # 초기 맵 리스트
# # for i in range(n):
# #     array.append(list(map(int,input().split())))
# # # 벽을 설치한 뒤의 맵 리스트    
# # temp = [[0] * m for _ in range(n)]

# # dx = [-1, 1, 0, 0] # 상하좌우
# # dy = [0, 0, -1, 1]
# # result = 0

# # def virus(x, y):
# #     for i in range(4):
# #         nx = x + dx[i]
# #         ny = y + dy[i]
# #         if nx < 0 or ny < 0 or nx >= n or ny >= m:
# #             continue
# #         if temp[nx][ny] == 0:
# #             # 해당위치에 바이러스 배치하고 재귀수행
# #             temp[nx][ny] = 2
# #             virus(nx,ny)

# # # 현재 맵에서 안전 영역의 크기 계산하는 매서드            
# # def get_score():
# #     score = 0
# #     for i in range(n):
# #         for j in range(m):
# #             if temp[i][j] == 0:
# #                 score += 1
# #     return score
# # # dfs이용해서 울타리 설치하면서 매번 안전 영역 크기 계산
# # def dfs(count):
# #     global result
# #     # 울타리가 3개 설치된 경우
# #     if count == 3:
# #         for i in range(n):
# #             for j in range(m):
# #                 temp[i][j] = array[i][j]
# #         # 각 바이러스의 위치에서 전파
# #         for i in range(n):
# #             for j in range(m):
# #                 if temp[i][j] == 2:
# #                     virus(i, j)
# #         # 안전영역의 최대값 계산
# #         result = max(result, get_score())
# #         return
# #     for i in range(n):
# #         for j in range(m):
# #             if array[i][j] == 0:
# #                 array[i][j] = 1
# #                 count += 1
# #                 dfs(count)
# #                 array[i][j] = 0
# #                 count -= 1

# # dfs(0)
# # print(result)