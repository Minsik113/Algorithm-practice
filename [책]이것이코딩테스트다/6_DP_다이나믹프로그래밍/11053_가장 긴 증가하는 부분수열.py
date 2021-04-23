'''
Longest increasing Subsequnce
'''
##########################################
##########################################
# 4/23 - O(NlogN)
# 아래문제가 i라면 0~i-1까지 순회해야했다.O(N) 
#   -> 이를 O(logN)시간 안에 찾아보자.
import bisect
n = int(input())
array = list(map(int, input().split()))

dp = [array[0]]

for i in range(n):
    if array[i] > dp[-1]: # 저장한숫자의 제일 끝보다 지금 나온게 크면-> 붙임
        dp.append(array[i])
    else:
        idx = bisect.bisect_left(dp, array[i]) # dp에서 array[i]가들어갈자리
        dp[idx] = array[i]

print(len(dp))
    
##########################################
##########################################
# 4/23 - O(N**2)
# i라면 0~i-1까지 순회해야한다.
n = int(input())
array = list(map(int, input().split()))

dp = [1] * (n)

for i in range(1, n):
    value = array[i]
    for j in range(0, i):
        if value > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
print(max(dp))