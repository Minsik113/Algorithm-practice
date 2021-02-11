'''
# 1/28
# 문제 난이도: Gold 5
# 문제 유형: DP, LCS(logest common subsequence)
# 추천 풀이 시간: 30분 (max 60분)

★★최장 공통 부분수열(LCS)★★
https://chanhuiseok.github.io/posts/algo-34/

두 수열이 주어졌을 때, 두 수열 모두의 부분 수열이 되는 수열 중 가장 긴것을 찾아라
LCS로 알려진 대표적인 DP문제
두 수열의 길이가 N미만일 때, O(N^2)로 해결가능

'''
'''
찾아낸 규칙
문자열을 비교하여 같았을 때

현재 칸에 들어갈 값은 대각선 왼쪽 위의 값 + 1 이다.
문자열을 비교하여 달랐을 때

현재 칸에 들어갈 값은 왼쪽과 위쪽의 값 중 더 큰 값이 들어간다.
이처럼 이전의 값이 앞으로 채워질 칸들에 대한 필요한 값이 되므로 DP로 볼 수 있습니다.
'''
string1 = input()
string2 = input()

length1 = len(string1)
length2 = len(string2)
dp = [[0] * (length1+1) for i in range(length2+1)]
num = 0

for i in range(1, length2 + 1):
    for j in range(1, length1 + 1):
        if string2[i-1] == string1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(max(dp[length2]))