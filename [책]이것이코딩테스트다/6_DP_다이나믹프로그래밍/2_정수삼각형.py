##########################################
##########################################
# 4/23
n = int(input())
array = []
array.append([int(input())])
for _ in range(n-1):
    array.append(list(map(int, input().split())))
# print(array)

for i in range(1, n):
    for j in range(len(array[i])):
        # 맨처음
        if j == 0:
            array[i][j] = array[i-1][j] + array[i][j]
        # 맨뒤
        elif j == len(array[i]) - 1:
            array[i][j] = array[i-1][j-1] + array[i][j]
        # 중간
        else:
            array[i][j] = max(array[i-1][j-1], array[i-1][j]) + array[i][j]

# print(array)
max_value = 0
for i in range(n):
    max_value = max(max_value, array[n-1][i])
print(max_value)

##########################################
##########################################
# 깔끔한 코드
# n = int(input())
# dp = []

# for _ in range(n):
#     dp.append(list(map(int, input().split())))

# # 2번째 줄부터 본다
# for i in range(1, n):
#     for j in range(i+1):
#         # 왼쪽 위에서 내려오는 경우
#         if j == 0:
#             up_left = 0
#         else:
#             up_left = dp[i-1][j-1]
#         # 바로 위에서 내려오는 경우
#         if j == i:
#             up = 0
#         else:
#             up = dp[i-1][j]
#         # 최대합 저장
#         dp[i][j] = dp[i][j] + max(up_left, up)
        
# print(max(dp[n-1]))


##########################################
##########################################
# 내풀이
'''
d[i] = max(왼쪽위, 바로위)
1. 바로위가 -1이 아닌 수들에 대해서 계산한다
2. 벽에 붙어있는경우는 바로 위만봄
3. 제일 밑의 max값 출력하면된다.

O(n^2)인데 n= 500이므로 충분하다.
'''

n = int(input())
array = [[-1]*n for _ in range(n)]
for i in range(n):
    data = list(map(int,input().split()))
    for j in range(0, i+1):
        array[i][j] = data[j]
# print(array)

# dp초기화
dp = [[-1]*n for _ in range(n)]
dp[0][0] = array[0][0]
# 현재 나온수가 이전 수보다 크면 이어붙임.
# 1. 바로위가 -1이 아닌 수들에 대해서 계산한다
# 2. 벽에 붙어있는경우는 바로 위만봄
# 3. 제일 밑의 max값 출력하면된다.
for i in range(1, n):
    for j in range(n):
        # 상관없는 수는 넘어감
        if array[i][j] == -1:
            continue
        # dp[i][j] 위치의 값 갱신해주면 된다.
        # 1번. '왼쪽 끝'인 경우 up_left = 0
        if j == 0: 
            up_left = 0
            up = dp[i-1][j]
        # 2번. '오른쪽 끝'인 경우. up =0
        if array[i-1][j] == -1: 
            up = 0
            up_left = dp[i-1][j-1]
        # 3번 '중간에 껴있는 경우는 up
        else:
            up = dp[i-1][j] 
            up_left = dp[i-1][j-1]
        # dp갱신
        dp[i][j] = max(up + array[i][j], up_left + array[i][j])
# print(dp)
print(max(dp[n-1]))