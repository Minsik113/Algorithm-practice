''' 시물레이션유형 == 완전탐색 == 구현
케릭터를 움직여야 한다는 의미에서 => 시물레이션 

상하좌우. 좌표이동
시작좌표(1,1) -> 최종좌표는?
-> 입력받은 문자가 뭔지 하나씩 이동하면된다.
'''
##########################################
##########################################
# 반복문으로 쉽게
n = int(input())
arrays = list(map(str, input().split()))

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]
directions = ['U', 'D', 'L', 'R'] # 상하좌우

x = 1 # 1~n까지
y = 1
for diect in arrays:
    nx, ny = 0, 0
    for i in range(len(directions)):
        if diect == directions[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x,y)
##########################################
##########################################
# 모든 조건문 생성
# n = int(input())
# data = list(map(str, input().split()))

# dx = [-1, 1, 0, 0] # 상 하 좌 우
# dy = [0, 0, -1, 1]
# directions = ['U', 'D', 'L', 'R'] # 상하좌우

# x = 1 # 1~n까지
# y = 1
# for i in range(len(data)):
#     if data[i] == 'U':
#         # 못 움직이는 경우
#         if x >= 2:
#             x -= 1
#     elif data[i] == 'D':
#         if x <= n-1:
#             x += 1
#     elif data[i] == 'L':
#         if y >= 2:
#             y -= 1
#     else:
#         if y <= n-1:
#             y += 1
# print(x,y)

