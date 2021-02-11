'''
# 1/23
# 문제 난이도: Silver 2
# 문제 유형: DP, LIS
# 추천 풀이 시간: 30분
'''
'''
가장 긴 증가하는 부분 수열(LIS) 문제는 전형적인 DP문제이다.
수열의  크기가 N일때, 기본적인 DP알고리즘으로 O(N^2)에 해결가능

D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
if array[j] < array[i]:
    D[i] = max(D[i], D[j]+1)
'''

n = int(input())
array = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]: # 이전꺼 < 현재나온거 = 수증가
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
