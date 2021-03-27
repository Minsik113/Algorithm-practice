'''
n = 100만이라 정렬하는건 아님.

'''
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))


##########################################
##########################################
# 2중포문으로 dp쓰는거 안됨
# '''
# 수열이 주어짐
# 가장 긴 증가하는 부분수열의 길이는?
# n = 100만


# -- 2중 for문은 불가능
# dp[i] = [i]가 들어갔을 떄 가장 긴 길이
# max(dp) = 할수있는 제일 긴 길이

# '''
# import sys
# input = sys.stdin.readline

# n = int(input())
# data = list(map(int, input().split()))

# dp = [1] * n # [i]가 가장 작을 수 있기 때문에 1로 초기화

# for i in range(1, n):
#     for j in range(0, i):
#         if data[i] > data[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(dp)