'''
# 1/29
# 문제 난이도:
# 출제 유형: DFS, BFS
# 추천 풀이 시간: 30분
'''
'''
연결 요소의 개수를 세는 문제이다.
DFS로 문제를 푸는 경우, sys라이브러리의 setrecursionlimit() 함수 설정
'''
from collections import deque

t = int(input())

def bfs(i,j):
    global count
    visited[i][j] = True
    q = deque()
    q.append([i,j])
    count = 0

    while q:
        i, j = q.popleft()
        count += 1
        if i-1 >= 1: # 위 1~h
           if array[i-1][j] == 1 and not visited[i-1][j]: 
               q.append([i-1,j])
               visited[i-1][j] = True
        if i+1 <= h: # 아래
           if array[i+1][j] == 1 and not visited[i+1][j]: 
               q.append([i+1,j])
               visited[i+1][j] = True
        if j-1 >= 0: # 왼 0~w-1
           if array[i][j-1] == 1 and not visited[i][j-1]: 
               q.append([i,j-1])
               visited[i][j-1] = True
        if j+1 < w: # 오른
           if array[i][j+1] == 1 and not visited[i][j+1]: 
               q.append([i,j+1])
               visited[i][j+1] = True

for _ in range(t):
    w, h, k = map(int, input().split()) # 너비 높이 배추수
    array = [[0]*w for i in range(h+1)]
    visited = [[False]*w for i in range(h+1)]
    result = []
    count = 0

    for i in range(k):
        xg, yg = map(int, input().split()) 
        array[yg+1][xg] = 1 # 첫줄은 비울꺼니까
    # (1,0) ~ (10,7) 까지있음 높이10 너비8

    for i in range(1, h+1):
        for j in range(w):
            if array[i][j] == 1 and not visited[i][j]: # 배추있으면 bfs돌아라
                bfs(i,j)
                result.append(count)
    print(len(result))
        
###################  ####################
# 나동빈
from collections import deque

t = int(input())

def bfs(i,j):
    visited[i][j] = True
    q = deque()
    q.append([i,j])
    directions = [(-1,0),(1,0),(0,-1),(0,1)] # 상 하 좌 우

    while q:
        a, b = q.popleft()
        for dx, dy in directions:
            i, j = a+dx, b+dy
            if i < 0 or i > h or j < 0 or j >=w:
                continue
            if array[i][j] and not visited[i][j]:
                q.append([i,j])
                visited[i][j] = True


for _ in range(t):
    w, h, k = map(int, input().split()) # 너비 높이 배추수
    array = [[0]*w for i in range(h+1)]
    visited = [[False]*w for i in range(h+1)]
    count = 0

    for i in range(k):
        xg, yg = map(int, input().split()) 
        array[yg+1][xg] = 1 # 첫줄은 비울꺼니까
    # (1,0) ~ (10,7) 까지있음 높이10 너비8

    for i in range(1, h+1):
        for j in range(w):
            if array[i][j] == 1 and not visited[i][j]: # 배추있으면 bfs돌아라
                bfs(i,j)
                count += 1
    print(count)
        


