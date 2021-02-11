'''
# 1/22
# 문제 난이도: Silver 1
# 문제 유형: 힙, 자료구조 (최소 힙)
# 추천 풀이 시간: 20분
'''
# 최소 힙 문제는 이해하고 있으면 됨.

import heapq, sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)

############  ############
# 동빈나
import heapq

n = int(input())
heap = []
result = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, x)

for data in result:
    print(data)



        