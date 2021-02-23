''' 시물레이션유형 == 완전탐색 == 구현
시물레이션 

상하좌우. 좌표이동
시작좌표(1,1) -> 최종좌표는?
-> 입력받은 문자가 뭔지 하나씩 이동하면된다.
'''

n = int(input())
array = input().split()
directions = ['U','D','L','R']
dx = [-1,1,0,0]
dy = [0,0,-1,1]
x, y = 1, 1
nx, ny = 0, 0
for plan in array:
    for i in range(4):
        if plan == directions[i]:
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 1 or ny < 1 or nx > n or ny > n: # 막혀서 못가는경우 무시
                continue
            x,y = nx, ny    
            print(x,y)
print(x, y)
        
