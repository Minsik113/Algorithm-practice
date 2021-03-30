'''
bfs로접근

nxn 체스판

'''
import sys
from collections import deque
input = sys.stdin.readline

# 8방위 10시,11시,1시,2시...
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]

for _ in range(int(input())):
    n = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    # 맵만들기
    data = [[0] * n for _ in range(n)]
    data[end_x][end_y] = 2 # target
    
    #
    flag = False
    q = deque()
    q.append((0, start_x, start_y)) # count, x, y
    data[start_x][start_y] = 1
    while q:
        count, x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위넘음 or 이미본곳
            if nx < 0 or ny < 0 or nx >= n or ny >= n or data[nx][ny] == 1:
                continue
            if data[nx][ny] == 2:
                count += 1
                flag = True
                break
            elif data[nx][ny] == 0:
                data[nx][ny] = 1
                q.append((count+1, nx, ny))
        if flag:
            print(count)
            break
    if not flag:
        print(0)