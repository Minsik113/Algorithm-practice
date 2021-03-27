# '''
# https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4#s-3.2
# 위사이트 참고
# 최장증가부분수열을 O(NlogN)로 풀 수 있다.
# 내가 풀던건 O(N^2)
# '''
# from bisect import bisect_left
# import sys
# input = sys.stdin.readline

# n = int(input())
# data = list(map(int, input().split()))
# dp = []

# for i in data:
#     k = bisect_left(dp, i) # dp리스트에 i가 들어갈 위치 k
#     if len(dp) <= k: # i가 가장 큰 숫자라면
#         dp.append(i)
#     else:
#         dp[k] = i # 자신보다 큰 수 중  최솟값과 대체


# ##########################################
# ##########################################
# # 2중포문으로 dp쓰는거 안됨
# # '''
# # 수열이 주어짐
# # 가장 긴 증가하는 부분수열의 길이는?
# # n = 100만


# # -- 2중 for문은 불가능
# # dp[i] = [i]가 들어갔을 떄 가장 긴 길이
# # max(dp) = 할수있는 제일 긴 길이

# # '''
# # import sys
# # input = sys.stdin.readline

# # n = int(input())
# # data = list(map(int, input().split()))

# # dp = [1] * n # [i]가 가장 작을 수 있기 때문에 1로 초기화

# # for i in range(1, n):
# #     for j in range(0, i):
# #         if data[i] > data[j]:
# #             dp[i] = max(dp[i], dp[j] + 1)
# # print(dp)