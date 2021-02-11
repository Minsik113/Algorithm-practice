'''
# 2/2
# 문제 난이도: Glod 1
# 문제 유형: 그리디
# 추천 풀이 시간: 10분

데드라인을 초과하는 문제는 풀 수 없다
데이터 개수(N)는 최대 200,000이다.
정렬 및 우선순위 큐를 이용하여 O(NlogN)
'''
'''
1. 데드라인을 기준으로 오름차순정렬
2. 각 문제의 '컵라면 수'를 우선순위 큐에 넣으면서, 데드라인을 
초과하는 경우에는 최소 원소를 제거한다.
'''

import heapq

n = int(input())
data = []
for i in range(1, n+1):
    deadline, food = map(int, input().split())
    data.append((deadline, food))
data.sort()

# print(data)
result = []

for i in data:
    a = i[0]
    heapq.heappush(result, i[1])
    if a < len(result): # 데드라인을 초과한다면 최소 원소를 제거
        heapq.heappop(result)
print(sum(result))
