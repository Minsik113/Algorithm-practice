# 조건 양옆집의 색이 달라야함
# 

# R G B
import time
start_time = time.time()
##########################################
##########################################
# # # # # # # # 코 드 넣 어 # # # # # # # #
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
##########################################
##########################################
end_time = time.time()
print(end_time-start_time)