'''
땅크기: nxn
r,c 나라에는 A[r][c]명이 살고있다.
 - 인구이동없을때까지 반복해라

1. 한번 쭉 보고 같은애들끼리 갱신한다
(단, 갱신 시 소수점 버림)
2. 갱신할게 없으면 나온다.
3. 몇 번을 반복했는지 출력한다.

'''
import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 1. 탐색시작
result = 0
while True:
    flag = False # 변동 체크하는 변수
    visited = [[True] * N for _ in range(N)] # 방문했는지 확인

    each_count = 0 # 그룹원 수
    total = 0 # 그룹원 총합
    possible = deque() # 바꿔줘야할 애들 좌표
    print('변경전',array)
    for x in range(N):
        for y in range(N):
            check = False # 인구이동 있는지 체크
            if not visited[x][y]:
                q = deque()
                q.append((x, y))
                possible.append((x,y))
                # 2. 해당도시에서 방문할 도시의 인접도시를 본다
                while q:
                    a, b = q.popleft()
                    visited[a][b] = True
                    total += array[a][b] # 대표값의 인구증가
                    for i in range(4):
                        nx = a + dx[i]
                        ny = b + dy[i]
                        # 범위넘거나 이미 본곳이면 다음꺼본다
                        if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny]:
                            continue
                        t = abs(array[nx][ny] - array[a][b])
                        # 3. 조건(L <= 인접한도시의 인구차 <= R)에 부합
                        if L <= t and t <= R:
                            check = True # 인구이동이 있다.
                            flag = True # 이번 사이클에 변한게 있다.
                            visited[nx][ny] = True # 3-1 방문했다고 체크
                            q.append((nx, ny))
                            possible.append((nx,ny))
                            each_count += 1 # 대표값의 개수증가
                    # 이동이 없었다면 다시 원상복구
                    if not check:
                        possible.popleft()
                        visited[a][b] = False
                        total -= array[a][b]
            # 인구이동이 있었다면 좌표위치애들을 다 바꿔준다
            if check:
                change = int(total / each_count)
                for a, b in possible:
                    array[a][b] = change
    # 4. 한 사이클끝났으니 이동이 있었나 보자
    if not flag: # 이동없었으면 나감
        break
    result += 1
    print(visited)
    print('변경후',array)
print(result)
    

