'''
array[i][j] = [i][j]에 올수있는 최대 값 
[i][j] = max([i-1][h-1],[i][h-1],[i+1][h-1]) 
'''
##########################################
##########################################
# 깔끔하게 푼 코드
for _ in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # dp 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index : index+m])
        index += m
    # 점화식 dp 시작
    for j in range(1, m): # 열부터 계산할것이므로 이렇게함
        for i in range(n):
            # '왼쪽 위'에서 오는 경우
            if i == 0: 
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # '왼쪽 아래'에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # '왼쪽'에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)

##########################################
##########################################
# 내풀이
import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    data = list(map(int, input().split())) # m개의열 n개의행 로 계산
    array = [[0]*m for _ in range(n)]
    # 예외처리 1개의 행일때
    if n == 1:
        print(sum(data))
        continue
    # 2차로 초기화
    for i in range(n):
        for j in range(m):
            array[i][j] = data[m*i+j]
        # print(data)
        # print(array)
        # print('--')
    # dp계산
    dp = [[0]*m for _ in range(n)] 
    for i in range(n): # '첫번째 열' 초기화
        dp[i][0] = array[i][0]
    print(dp)
    for j in range(1, m): # '두번째 열'부터 적용
        for i in range(n):
            if i == 0: # '맨윗쪽 행' 이라면 왼쪽, 왼쪽아래만 본다
                dp[i][j] = max(dp[i][j-1]+array[i][j], dp[i+1][j-1]+array[i][j])
            elif i == (n-1): # '맨아래 햇'이라면 왼쪽, 왼쪽위만 본다
                dp[i][j] = max(dp[i][j-1]+array[i][j], dp[i-1][j-1]+array[i][j])
            else: # '중간'에 껴있다면 왼쪽, 왼쪽위, 왼쪽아래 본다.
                dp[i][j] = max(dp[i][j-1]+array[i][j], dp[i-1][j-1]+array[i][j], dp[i+1][j-1]+array[i][j])
        print(dp)
    # 제일 끝 열의 max값을 출력한다
    max_value = 0
    for i in range(n):
        if dp[i][m-1] > max_value:
            max_value = dp[i][m-1]
    print(max_value)

