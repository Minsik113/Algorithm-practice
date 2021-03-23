'''
맵: nxn 
m마리의 물고기
(시작)아기상어크기 2
상하좌우로 이동

현재위치에서 도달가능한 물고기들 중 먹을 수 있는애들을 봐야한다 
1. 먹을 수 있는 물고기가 없다면 -> 엄마상어
2. 먹을 수 있는 물고기 1개 -> 먹으러간다
3. 먹을 수 있는 물고기가 2개이상 -> 거리가 가까운 물고기 먹으러감
(위쪽, 왼쪽 에 우선순위를 둔다)

먹으면 빈칸이됨.
먹은수(count)가 자신의 크기와 같아지면 크기 +1
엄마상어부를때까지 걸리는 초는?
'''
from collections import deque
import heapq

n = int(input())

# 맵 입력받자
array = [list(map(int, input().split())) for _ in range(n)]

# 아기상어 위치, 물고기 들어있는 곳
start_pos = [0,0]
fish = [] # 물고기들 무게 1~6,좌표
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            start_pos[0], start_pos[1] = i,j
            # array[i][j] = -2 # 상어표시
        elif array[i][j] != 0:
            heapq.heappush(fish, (array[i][j], i, j))

print(fish)
exit()
# 현재위치에서 도달가능한 물고기들 중 먹을 수 있는애들을 봐야한다
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# fish = (물고기크기, 좌표)
# 현재위치에서 먹을 수 있는애 찾아보자
result = 0 # 전체 걸린시간

q = deque()
q.append((0, start_pos[0], start_pos[1])) # 좌표, 시간
now = 2
possible = deque() # 현재 먹을 수 있는 애들
while True:
    while q: # (여기까지걸리는시간, 좌표)
        time, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 이동가능한 애들중에서 먹을 수 있는애 찾자
            if array[nx][ny] == 0:
                q.append((time+1, nx, ny))
            elif array[nx][ny] <= now: # 현재무게에서 먹을수있는애들
                possible.append((time+1, nx, ny)) # 
                q.append((time+1, nx, ny))
    # 먹을 수 있는애들의 개수가 1 or 2이상
    if len(possible) == 0: # 종료
        print(result)
        break

    possible.sort() # 오름차순 순서로 됨
    elif len(possible) >= 1:
        while possible: # 가능한애들 다 먹는다
            zzz = possible.popleft() # 제일 조금걸리는애한테 감.
            result += zzz[0] # 전체시간 증가시키고,
            # 갈수있는애들중 가까운애한테 다시가야함
            for

        # 좌표이동 시키고
        # 물고기 위치 0으로바꾸고
        # count + 1 . 몸집커지나도봐야함

