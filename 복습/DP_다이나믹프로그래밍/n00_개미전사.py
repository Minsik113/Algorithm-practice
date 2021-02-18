# '''
# 1. 경우의 수는 2가지 (선택한다. 안한다)
# 선택 한다   -> d[1]~d[i-2]중 가장 큰 수 + array[i]
# 선택 안한다 -> d[1]~d[i-1]중 가장 큰 수
# d[i] = max(max(array[:i-1]) + array[i], max(array[:i])) 

# d[i] = max(d[i-1], d[i-2]+array[i])
# '''
# n = int(input())
# array = list(map(int, input().split()))
# dp = [0] * (n)
# dp[0] = array[0]
# dp[1] = max(array[0],array[1])

# for i in range(2, len(array)): #
#     dp[i] = max(dp[i-1], dp[i-2]+array[i])
# print(dp)
