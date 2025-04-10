'''
날짜: 2025.04.07
링크: https://www.acmicpc.net/problem/9465
시간복잡도: 

1.학습키워드
dp

2.문제
첫번째열에서 시작 -> 대각선으로 이동
두번째열에서 시작 

3.어떤 문제가 있었고, 나는 어떤 시도를 했는지
전체문제를 쪼개야한다.

4.어떻게 해결했는지

5.무엇을 새롭게 알았는지
dp가 어렵다면 재귀문제를 익히자.

'''

# 1.입력받기
T = int(input())
for i in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    
    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        
    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    
    print(dp[max(dp[0][n-1]), dp[1][n-1]])
