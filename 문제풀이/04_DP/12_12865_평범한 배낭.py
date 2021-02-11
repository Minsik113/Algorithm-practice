'''
# 1/23
# 문제 난이도: Gold 5
# 문제 유형: DP
# 추천 풀이 시간: 30분

Knapsack Problem으로 알려져있는 문제
물품의 수: N, 배낭에 담을 수 있는 무게: K
O(NK)로 문제해결가능
'''
'''
핵심 아이디어: 모든 무게에 대하여 최대 가치를 저장하기.
D[i][j] = 배낭에 넣은 물품의 무게 합이 j일 때 얻을 수 있는 최대 가치
각 물품의 번호 i에 따라서 최대 가치 테이블 D[i][j]를 갱신하여 문제 해결가능
'''
# 2차원배열에 넣고 하겠다.

n, k = map(int, input().split()) # 최대 101개물건
dp = [ [0]*(k+1) for _ in range(n+1) ] # 0 ~ n개

for i in range(1, n+1): # 1 2 3 4 
    weight, value = map(int, input().split())

    for j in range(1, k+1): # 1 2 3 4 5 6 7
        if j < weight: # 그대로
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
print(dp[n][k])
        


