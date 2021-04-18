'''
17:45 ~ 
x -> y로 토네이도가 이동할때
y의 모래가 모두 이동한다
    a는 (y - (비율써있는곳의모래))만큼 쌓인다.

토네이도는 (0,0)이나 밖으로나가면 소멸.

'''
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y = n//2, n//2

visited = [[False] * n for _ in range(n)]
visited[start_x][start_y] = True
percentage = [ [0, 0, 0.02, 0, 0] \
            , [0, 0.1, 0.07, 0.01, 0] \
            , [0.05, 0.55, 0, 0, 0] \
            , [0, 0.1, 0.07, 0.01, 0] \
            , [0, 0, 0.02, 0, 0]]

# 왼쪾으로 90도회전 
def rotate_left90(array):
    r_x, r_y = 0, 0
    rotate_array = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if n-1-j == start_x and i == start_y:
                r_x, r_y = i, j
            rotate_array[i][j] = array[n-1-j][i]
    return rotate_array, r_x, r_y

# x=(a,b)임 모래양 계산 비율에 넣어서 계산하는 함수
def calculate(a, b, data):
    # y좌표
    na, nb = a, b-1
    if na - 2 >= 0:
        array[na-2][nb] += int(array[na][nb] * 0.02)
    if na - 1 >= 0:
        array[na-2][nb] += int(array[na][nb] * 0.02)
        
    pass

# 맨처음은 예외로 서쪽으로이동
print('www')
# 현재위치에서 아래의 visited가 False라면 방향꺾는다.
while not (start_x == 1 and start_y == 1):
    x = start_x + 1 # '현재의 아래' 위치좌표
    y = start_y + 0
    # 이미 본 곳 -> 지금방향그대로 서쪽으로 진행
    if visited[x][y]:
        calculate(start_x, start_y, array) # 현재 토네이도위치
        start_y = start_y - 1 # 현재위치이동

    # 본곳이 아니라면 꺾는다.
    else:
        # 1. 방향 돌리고 서쪽본다
        array, start_x, start_y = rotate_left90(array) # 회전했으니 좌표도변함
        # 2. 모래 뿌린다.
        calculate(start_x, start_y, array) # 현재토네이도위치
        start_y = start_y - 1 # 현재위치이동

