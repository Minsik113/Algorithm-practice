'''
2개풀이 같음
다만, 조건을 잘보자.
-> exit()안쓰는쪽이 좋아보인다.
'''

##########################################
##########################################
# 조건 잘보자. 
import heapq # 그당시 제일 작은거 2개 더해야함

n = int(input())
array = []
for i in range(n):
    heapq.heappush(array, int(input()))

total = 0
while len(array) != 1:
    a = heapq.heappop(array)
    b = heapq.heappop(array)
    c = a+b
    total += c
    heapq.heappush(array, c)

print(total)
##########################################
##########################################
# 내풀이
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