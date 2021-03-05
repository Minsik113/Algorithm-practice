n = int(input())
dp = [0] * (n+1) # 0~n

# 예외처리
if n == 1:
    print(1)
    exit()
if n == 2:
    print(3)
    exit()
dp[1] = 1 # 2x1인 경우엔 1가지 블럭만 사용가능
dp[2] = 3 # 총 3가지 경우가 있으므로
for i in range(3, n+1):
    dp[i] = (dp[i-1] + (2 * dp[i-2]) )% 796796

print(dp)
print(dp[n])
