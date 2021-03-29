'''
하루에 익은 토마토 근처에 있는 토마토들이 익는다.
창고에 보관된 토마토들이 며칠이 지나면 다 익는가??

상하좌우 위아래 - 6방향

bfs로 계속퍼트린다 변화가없으면 종료
1 = 익은토마토
0 = 익지않은 토마토
-1 = 토마토없음

1. 1존재
    0이없다 -> 0
    0이있다 -> 
'''
from collections import deque

m, n, h = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n*h)]
data = []
start = deque()
flag = True
for i in range(n*h):
    a = list(map(int, input().split()))
    # 익은 토마도 위치
    for k in range(m):
        if a[k] == 1:
            start.append((0, i, k)) # 일수,좌표
        elif a[k] == 0:
            flag = False
    data.append(a)

# 예외처리 1
# 모든토마토가 익어있는 상태 -> 0이 없는경우 = 0
if flag: # 0을발견못할때 
    print(0)
    exit(0)

result = 0
dx = [-1,1,0,0,n,-n] # 상,하,좌,우,위,아래
dy = [0,0,-1,1,0,0] 
pre = 0
while start:
    day, x, y = start.popleft() # (행,열)
    if day != pre:
        result += 1
        pre = day
    # 같은층 애들을 비교한다
    for i in range(6): # 상하좌우 한칸아래 한칸위
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 벗어남 or 토마토를 익힐수 있는곳이 아님
        if nx < 0 or ny < 0 or nx >= n*h or ny >= m or data[nx][ny] != 0:
            continue
        # 범위안 + 6방위 중에서 0인경우만
        data[nx][ny] = 1 
        start.append((day+1, nx, ny))

# 예외처리2
# 토마토가 모두 익지는 못하는 상황이라면 -> 0이존재한다
flag = True
for i in range(n*h):
    for j in range(m):
        if data[i][j] == 0:
            flag = False

# print(data)
if not flag:
    print(-1)
else:
    print(result)
