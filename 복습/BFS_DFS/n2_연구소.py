# '''
# 벽3개 설치한 모든 경우를 다 본다.

# '''
# 64C3하면 60^3 약22만번
# 3개 들어갈 수 있는 곳에 벽을 다 설치 
# '2' 퍼트리기
# 0의 개수세기

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
temp = [[0]*m for _ in range(n)] # 바이러스 증식시키고 원상복구시킬 맵

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]
result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx,ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score
# dfs이용해서 울타리짓고, 안전영역 개수 세기
# import copy
def dfs(count):
    global result
    if count == 3: # 안전지대 개수세자
        # temp = copy.deepcopy(array)
        for i in range(n):
            for j in range(m):
                temp[i][j] = array[i][j]
        # 각 바이러스의 위치에서 전파
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전영역크기 계산
        result = max(result, get_score())
        return
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                array[i][j] = 1
                count += 1
                dfs(count)
                count -= 1
                array[i][j] = 0
    
dfs(0)
print(result)
# n, m = map(int, input().split()) # n높이 m너비
# array = [] # 초기 맵 리스트
# for i in range(n):
#     array.append(list(map(int,input().split())))
# # 벽을 설치한 뒤의 맵 리스트    
# temp = [[0] * m for _ in range(n)]

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
#             # 해당위치에 바이러스 배치하고 재귀수행
#             temp[nx][ny] = 2
#             virus(nx,ny)

# # 현재 맵에서 안전 영역의 크기 계산하는 매서드            
# def get_score():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#     return score
# # dfs이용해서 울타리 설치하면서 매번 안전 영역 크기 계산
# def dfs(count):
#     global result
#     # 울타리가 3개 설치된 경우
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = array[i][j]
#         # 각 바이러스의 위치에서 전파
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i, j)
#         # 안전영역의 최대값 계산
#         result = max(result, get_score())
#         return
#     for i in range(n):
#         for j in range(m):
#             if array[i][j] == 0:
#                 array[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 array[i][j] = 0
#                 count -= 1

# dfs(0)
# print(result)