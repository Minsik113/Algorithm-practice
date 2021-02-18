test = int(input())
for _ in range(test):
    N = int(input())
    dp = [0] * (N+1) # 1~N까지
    if N >= 1 and N <= 3:
        print(1)
    elif N >= 4 and N <= 5:
        print(2)
    else:
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2
        for i in range(6, N+1):
            dp[i] = dp[i-1] + dp[i-5]
        print(dp[N])