'''
2025.05.03
https://www.acmicpc.net/problem/2667
단지번호붙이기 

총단지수, 각단지의 개수
'''
import sys
from collections import deque
#input = sys.stdin.readline

def bfs(a,b):
    q = deque()
    q.append((a,b))
    arr[a][b] = 0 # 다시 안보려고
    cnt = 1
    
    while(q):
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny]==1:
                cnt += 1
                q.append((nx,ny))
                arr[nx][ny] = 0
    
    result.append(cnt)

n = int(input())
arr = [list(map(int,input())) for _ in range(n)] # n x n
result = [] # 단지별로 집 개수를 세기위해
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            bfs(i,j)


result.sort()
print(len(result))
for i in result:
    print(i)