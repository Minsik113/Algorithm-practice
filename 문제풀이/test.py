n = int(input())
plans = input().split()
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1] 
x, y = 1, 1
move_type = ['U','D','L','R']

for plan in plans:
    nx, ny = 0, 0
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = dx[i] + x
            ny = dy[i] + y
            print('dd이동',nx, ny)
            
        
    if nx < 1 or ny < 1 or nx > n or ny >n:
        continue
    x, y = nx, ny
    print('이동',x, y)
print(x, y)