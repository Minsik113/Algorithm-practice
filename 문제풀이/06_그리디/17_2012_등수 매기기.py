'''
# 1/31
# 문제 난이도: Silver 3
# 문제 유형: 그리디
# 추천 풀이 시간: 20분

그리디 = 이 문제를 풀기위한 핵심 아이디어 하나를 떠올리면 된다.
예상 등수를 오름차순으로 정렬하자.
'''

############## #############
# 나동빈
import sys
input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    data.append(int(input()))
data.sort()

result = 0 

for i in range(1, len(data)+1):
    result += abs(i - data[i-1])
print(result)

    
