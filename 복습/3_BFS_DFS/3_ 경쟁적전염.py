'''
1. S초후에 (x,y) 에 존재하는 바이러스 출력하라
2. 없으면 0출력

-> 바이러스 종류 오름차순리스트로 정렬.
각 바이러스마다 bfs한번씩한다.
'''
from collections import deque 

n, k = map(int, input().split()) # nxn, k개의바이러스
array = [] # 1~n
virus_type = [0] * 1001 # 1~1000
save_pos = []
for i in range(n):
    array.append(list(map(int, input().split())))
time, x, y = map(int, input().split())

for i in range(n):
    for j in range(n):
        if array[i][j] != 0:
            save_pos.append((i,j,array[i][j],0)) # (x,y,바이러스번호,초)

# 바이러스 번호로 오름차순정렬
save_pos.sort(key=lambda x:x[2]) 

# 바이러스 번호 순으로 bfs시작
dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]
# 리스트 -> deque로 변환
save_pos = deque(save_pos)

while save_pos:
    now = save_pos.popleft()
    row, col, virus, t = now[0], now[1], now[2], now[3] # 좌표,virus번호
    if t == time: # 다봤으므로
        break
    # print(row,col,virus)
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        # 옮길 수 있으면 옮기자
        if array[nx][ny] == 0:
            array[nx][ny] = virus
            save_pos.append((nx,ny,virus,t+1))

# print(array)
print(array[x-1][y-1])
