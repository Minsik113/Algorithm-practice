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
    