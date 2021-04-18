##########################################
##########################################
# 4/18 - 내풀이
'''
1시간40분걸림 ;; 
주사위 모양: 정육면체
지도값     0 : 주사위의 바닥면의 숫자가 지도에 복사됨
지도값 NOT 0 : 주사위의 바닥면의 숫자가 지도값으로 복사되고 0으로 바뀜

매번 주사위 상단의 값을 출력해라.(범위넘어가면 무시)
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m, start_x, start_y, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
direct = list(map(int, input().split()))
# print(array)
# print(direct)

dx = [0, 0, 0, -1, 1] # x 동 서 북 남
dy = [0, 1, -1, 0, 0]
dice_sn = deque([0] * 4) # 주사위 남, 북 - 바닥면이 맨끝임.
dice_ew = deque([0] * 3) # 주사위 동, 서
def func1(x, y, index):
    global start_x, start_y
    nx = x + dx[index]
    ny = y + dy[index]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        return -1
    start_x, start_y = nx, ny
    
    # 1. 남북 or 동서 인지 방향을 체크한다
    if index == 3 or index == 4: # 남북 -> dice_sn
        if index == 3: # 북
            dice_sn.append(dice_sn.popleft()) # 맨앞빼서 맨뒤로
        else: # 남
            dice_sn.appendleft(dice_sn.pop()) # 맨뒤빼서 맨앞으로

        if array[nx][ny] == 0: # 지도 0
            array[nx][ny] = dice_sn[-1]
        else: # 지도 not 0
            dice_sn[-1] = array[nx][ny]
            array[nx][ny] = 0
        dice_ew[1] = dice_sn[1]
    else: # 동서 -> dice_ew
        if index == 1: # 동
            # dice_sn의 맨뒷값이 dice_ew의맨처음으로
            dice_ew.appendleft(dice_sn.pop())
            dice_sn.append(dice_ew.pop())
        else: # 서
            dice_ew.append(dice_sn.pop())
            dice_sn.append(dice_ew.popleft())
        if array[nx][ny] == 0: # 지도 0
            array[nx][ny] = dice_sn[-1]
        else: # 지도 not 0
            dice_sn[-1] = array[nx][ny]
            array[nx][ny] = 0
        dice_sn[1] = dice_ew[1]
    # 지도좌표옮겼고, 주사위좌표옮겻고 값바꾸자
    
    # 하늘보는면 출력
    return dice_sn[1]

for d in direct:
    temp = func1(start_x, start_y, d)
    # print('남북',dice_sn)
    # print('동서',dice_ew)
    if temp != -1:
        print(temp)

