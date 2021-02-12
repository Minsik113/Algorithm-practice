'''
0. 4방위를 본다.
1. 보는위치의 왼쪽을 먼저 찾는다.
-> dfs(보는위치?, depth?)
2. 모두 가본방향이라면 지금보는방향에서 뒤로 간다.
-> 가봤는지 check하는 맵 만들기
3. 2번에서 뒤가 바다라면 끝낸다.
4. 움직인 블럭 수는?
'''
##########################################
##########################################
# while로구성
n, m = map(int, input().split())
start_x, start_y, direct = map(int, input().split())
d = [[0] * m for i in range(n)] # 방문한 위치 저장하기 위한 맵
d[start_x][start_y] = 1

array = [] # 전체 맵 
for i in range(n):
    array.append(list(map(int, input().split())))
dx = [-1, 0, 1 ,0] # 북 동 남 서
dy = [0, 1, 0, -1]

def turn_left():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3

count = 1
turn_time = 0 # 4번다 봤는지 체크하려고
x, y = start_x, start_y
while True:
    turn_left()
    nx = x + dx[direct]
    ny = y + dy[direct]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny 
        count += 1
        turn_time =0
        continue
    else:
        turn_time += 1
    # 네방향 모두 갈수없는겨우 = 뒤로이동
    if turn_time == 4:
        nx = x - dx[direct]
        ny = y - dy[direct]
        # 갈수있다면이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 갈수없다면 나옴
        else:
            break
        turn_time = 0
print(count)
            
##########################################
##########################################
# 재귀이용. 방향을 4방향씩 보게끝 dfs구성
n, m = map(int, input().split())
start_x, start_y, direct = map(int,input().split())
world = [list(map(int, input().split())) for _ in range(n)] # n x m (0,0)~(n-1,m-1)
# visited = [[False]*m for i in range(n)]
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]
count = 0
world[start_x][start_y] = 2

def dfs(now_x, now_y, direct):
    global count
    count += 1
    if direct < 0: # 북쪽(0)시작면 -1됨. 그걸 서쪽봐야해서 (3)으로바꿔줌
        direct = 3
    # 현재위치에서 왼쪽부터보고 4방위본다.
    for i in range(direct, -(4-direct),-1):
        nx = now_x + dx[i] # 0-1은 맨뒤니까 됨.
        ny = now_y + dy[i]
        # print(i,'볼수있는곳',nx,ny)

    # 갈 수 없다면 방향만돈다.
        if (nx < 0 or ny < 0 or nx >= n or ny >= m): # 막힘
            pass
    # 갈 수 있으면 봤던곳인지 체크
        else:
            # print('여기체크할거야')
            # print(',,',i,nx,ny)
            # print(world[nx][ny])
            if not world[nx][ny]: 
                # print(i,'보는곳',nx,ny)
                world[nx][ny] = 2
                dfs(nx,ny,i-1) # 방위꺾어서 또봄.
    return

dfs(start_x, start_y, direct-1) # 북쪽시작이면 그 왼쪽봐야함
# print(world)
print(count)
