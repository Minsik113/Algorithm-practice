'''
# 1/27
# 문제 난이도: Silver 1
# 문제 유형: DP
# 추천 풀이 시간: 40분
'''
'''
차례대로 곡을 연주한다는 점에서 DP로 해결할 수 있는 문제
N(곡의 개수), M(볼륨의 최댓값)이다.
DP를 이용하여 O(NM)으로 해결가능

모든 볼륨에 대하여 연주 가능 여부를 계산해라
D[i][j+1] = i번째 노래일 떄 j크기의 볼륨으로 연주 가능한가?
if D[i-1][j] = True:
    D[i][j-V[i]] = True
    D[i][j+V[i]] = True
'''
n, s, m = map(int, input().split())
array = list(map(int, input().split()))

dp = [[0]*(m+1) for i in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1): # dp[i][j] #첫행은 0 
        # 0일때
        if dp[i-1][j] == 0:
            continue
        # array와 더해보자
        if j - array[i-1] >= 0:
            dp[i][j-array[i-1]] = 1
        if j + array[i-1] <= m:
            dp[i][j+array[i-1]] = 1

result = -1
for i in range(m,-1,-1):
    if dp[n][i] == 1:
        result = i
        break
print(result)

################  ###############
# 나동빈
n, s, m = map(int,input().split())
data = list(map(int, input().split()))

dp = [[0]* (m+1) for i in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] == 0: # 0행 5 -> 시작위치= 5니까
            continue
        if j - data[i-1] >= 0:
            dp[i][j-data[i-1]] = 1
        if j + data[i-1] <= m:
            dp[i][j+data[i-1]] = 1        
    print(dp[i])

result = -1
for i in range(m,-1,-1): # 볼륨중 가장큰값부터 1인지 확인하기
    if dp[n][i] == 1:
        result = i
        break
print(result)

