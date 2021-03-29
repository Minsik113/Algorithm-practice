'''
d[i] = 금액i를 만들 수 있는 최소한의 화폐 개수
k = 각 화폐의 단위
점화식: 각 화폐 단위인 k를 하나씩 확인하며
dp[i-k]를 만드는 방법이 존재하면, dp[i]  = min(dp[i], dp[i-k]+1)
dp[i-k]를 만드는 방법이 존재하지 않는다면, dp[i] = int(1e9)

'''
########################################
########################################
#
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

dp = [10001] * (m+1) # m개로 다 체크해볼것이다.
dp[0] = 0 

for i in range(n):
    for j in range(array[i], m+1):
        if dp[j-array[i]] != 10001:
            dp[j] = min(dp[j], dp[i-array[i]]+1)
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

########################################
########################################
'''1. 동전내림차순
2. 앞부터 하나씩 뺄수있으면 뺸다.
3. -해서 0이되면 끝 
4. 모든수 뻇는데 0이아니라 음수로가면 -1출력
-> 내풀이 - 그리디 - 이렇게 풀면안된다네?

-> 정렬 O(nlogn) = 200 (n=10^2니까)
-> m번을 다 봐야함 O(M) = 10^4
-> O(M x NlogN) = 2x10^6 충분하지않나.?
'''
# n, m = map(int, input().split())
# array = []

# for _ in range(n):
#     array.append(int(input()))
# array.sort(reverse=True)

# count = 0
# for i in range(n):
#     temp = m // array[i]
#     if temp != 0: # array[i]보다크면 그만큼 뺴줌
#         m -= temp*array[i]
#         count += temp
# if m == 0:
#     print(count)
# else:
#     print(-1)
