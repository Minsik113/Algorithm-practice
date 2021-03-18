# '''
# 청소한 칸의 개수를 세라
# '''
# n, m = map(int, input().split())
# r, c, d = map(int, input().split())

# # 그래서 청소할곳이 북0->서 동1->북 
# dx = [0,-1,0,1] # 서북동남
# dy = [-1,0,1,0]

# # 맵 입력받음
# array = [list(map(int, input().split())) for _ in range(n)]
def turn(direction):
    now = (direction - 1) % 4
    return now
for i in [1,2,3,4,5,6,7,0]:
    print(turn(i))

# # 회전하는 함수
# def turn(direction):
#     now = (direction - 1) % 4
#     return now
# # 시작
# def simulate(r,c,d):
#     count = 0 # 청소한 칸의 개수를 센다.
#     index = 0 # 4번을 모두보면 후진한다.
#     direction = d
#     x, y = r, c
#     if array[x][y] == 0: # 청소 가능하면 청소해라
#         array[x][y] = 2 
#         count += 1

#     # 바라보는 방향에서 왼쪽을 본다
#     while True:
#         # 4방향 다 돌았는데 막혀있다면 후진한다.
#         if index == 4:
#             print('q',x,y,direction)
#             index = 0 # 초기화해주고
#             x = x - dx[direction] # 현재 위치 이동
#             y = y - dy[direction]
#             # 후진할때 벽 or 범위 밖
#             if nx < 0 or ny < 0 or nx >= n or ny >= m or array[nx][ny] == 1:
#                 break
#             # 후진할때 청소한곳이라면
#             if array[nx][ny] == 2:
#                 continue # 현재위치 바꾸고 다시봄
        
#         nx = x + dx[direction]
#         ny = y + dy[direction]
#         # 범위안에 있다
#         if nx >= 0 and ny >= 0 and nx < n and ny < m:
#             # 범위안 -> 청소 할 수 있다면 
#             if array[nx][ny] == 0:
#                 array[nx][ny] = 2 # 청소하고
#                 x, y = nx, ny # 현재위치를 이동한다.
#                 count += 1 # 청소햇으니 센다.
#                 index = 0 # 청소카운트 초기화
#             # 범위안 -> 벽 or 청소
#             if array[nx][ny] != 0:
#                 index += 1 # 하나 세주고 
#             # 확인했으니 방향바꿔준다
#             direction = turn(direction) 

#         # 범위밖이라면 방향 회전
#         else:
#             index += 1
#             direction = turn(direction)
#     return count

# print(simulate(r,c,d))

            

