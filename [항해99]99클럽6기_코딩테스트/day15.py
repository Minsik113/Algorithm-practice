'''
날짜: 2025.04.20
링크: https://www.acmicpc.net/problem/17271
시간복잡도: 

1.학습키워드
최단거리로 생각하면되나? a,b중 b의 개수를 0개부터 @개까지 의 조합으로 구할 수 있을거같은데? => N이 10000개라 안됨
dp

2.문제
N초동안 사용할 수 있는 스킬조합의 개수는? A스킬은 1초, B스킬은 M초이다

3.어떤 문제가 있었고, 나는 어떤 시도를 했는지
B스킬이 나올 수 있는 경우의수를 순열로 섞어라. => 생각보다 너무많은데?
안보일때는 경우의 수 적으면서 해보자. -> dp

4.어떻게 해결했는지
dp로 나올 수 있는 경우의 수 작성

5.무엇을 새롭게 알았는지
중복순열라이브러리 = product

#99클럽 #TIL #개발자취업 #코딩테스트준비 #코테연습 #항해99 #코테

'''
'''
i초 때 가능한 경우의 수
1)i-1초까지 스킬 쓴 상태에서 A스킬 사용
2)i-M초까지 스킬 쓴 상태에서 B스킬 사용(i>=M 일때)
dp[i] = dp[i-1]+dp[i-M]
'''

import sys
input = sys.stdin.readline

# 1.입력받기
n, m = map(int, input().split())
dp = [1] * (n+1)

# 2. 가능한 경우 세기
for i in range(m, n+1): # m초미만일때는 무조건 1이다. dp[i] = dp[i-1]
    dp[i] = (dp[i-1] + dp[i-m]) % 1000000007

print(dp[n])
