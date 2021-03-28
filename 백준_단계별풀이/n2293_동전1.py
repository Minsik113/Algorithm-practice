# '''
# n가지동전 합이 k
# n=100 k=10000

# 코인 수 제한 없음.  
# [1,2,5]코인이있음 k = 10

# dp[i] = i를 만들 수 있는 경우의 수

# '''
# n, k = map(int, input().split())
# coins = [int(input()) for x in range(n)]
# dp = [0] * (k+1)
# check = [False] * (k+1) # 금액이 i일때 만들 수 있는가를 체크

# # 1~k원까지 경우의 수를 구할것이다
# for i in range(1, k):



