'''
# 1/22
# 문제 난이도: Gold 4
# 문제 유형: 힙, 자료구조, 그리디
# 추천 풀이 시간: 20분
'''
# 제일 작은것끼리 pop하고 더한값을 다시 리스트에 넣음.
# 반복한다.
# 이때의 값을 구해라
# 정렬하는데에 O(logn) + 찾는데에 O(1)
# 시간복잡도: O(logn)
#
############  ############
import heapq 

n = int(input())
data = []
result = 0

for _ in range(n):
    data.append(int(input()))

heapq.heapify(data)

while len(data) > 1: # 다 합쳐서 1개남으면 그거 출력
    x1 = heapq.heappop(data)
    x2 = heapq.heappop(data)
    x3 = x1 + x2
    result += x3
    heapq.heappush(data, x3)

print(result)

############  ############
# 나동빈