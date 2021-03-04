'''
리스트들 중 제일작은 2개를 더해서 다시넣는다.
1. 우선순위큐(heapq)쓰면될듯
2. len(q) == 1이면 종료

'''

import sys, heapq
input = sys.stdin.readline

n = int(input())
h = []
for i in range(n):
    heapq.heappush(h, int(input()))

# 예외처리
if n == 1:
    print(0)
    exit(0)

# 탐색시작
result = 0
while (len(h) >= 2):
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    result += (a + b)
    heapq.heappush(h, a + b)
print(result)