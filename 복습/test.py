'''
전형적인 dp아이디어인 LIS (가장 긴 증가하는 부분 수열)문제이다.
본 문제는 가장 긴 감소하는 부분 수열을 찾는 문제로 치환 가능하다.
-> LIS 알고리즘을 조금 수정하여 적용하면 정답도출가능

D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
0 <= j < i 에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
-> 가장 긴 증가하는 부분 수열이니까  array[j] < array[i] 이다.
=> O(N^2)

이렇게 나온 D의 값은 우리가 만들 수 있는 증가하는 부분수열 중에서 가장 긴 수열의 길이가 저장되어있다.
-> 병사 정보의 순서를 뒤집고, LIS적용하면됨
'''
n = int(input())
array = list(map(int, input().split()))
# 증가하는 순서로 만들기 위해
array.reverse()

# dp초기화
dp = [1] * (n)
# LIS수행
for i in range(1, n):
    for j in range(0,i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp)

# n = int(input())
# array = list(map(int, input().split()))
# # 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
# array.reverse()

# # dp 초기화
# dp [1] * n
# # LIS수행
# for i in range(1, n):
#     for j in range(0, i):
#         if array[j] > array[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(n - max(dp))



