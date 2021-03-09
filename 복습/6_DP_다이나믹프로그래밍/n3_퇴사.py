# '''
# 거꾸로봐라?
# dp[i] = 끝날때까지 가질 수 있는 최대 금액
# '''
# n = int(input())
# t = [] # 기간
# p = [] # 금액
# for _ in range(n):
#     a, b = map(int, input().split())
#     t.append(a)
#     p.append(b)

# # dp 초기화
# dp = [0] * (n+1) # dp[i] = i일에서 끝날때까지 가질 수 있는 최대금액

# # dp시작
# max_value = 0
# for i in range(n-1, -1, -1): # i는 현재 일
#     time = i + t[i] # 현재일수 + 걸리는기간
#     # 기간안에 못함
#     if time > n:
#         dp[i] = max_value
#     # 기간안에 함 -> 현재까지 최대 금액 저장
#     else:
#         dp[i] = max(max_value, dp[time] + p[i])
#         max_value = dp[i]
# print(max_value)
