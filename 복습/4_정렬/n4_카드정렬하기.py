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
import heapq # 그당시 제일 작은거 2개 더해야함

n = int(input())
array = []
for i in range(n):
    heapq.heappush(array, int(input()))

if n==1:
    print(0)
    exit()

total = 0
while len(array) >= 2:
    a = heapq.heappop(array)
    b = heapq.heappop(array)
    total += a+b
    # print(a,b,a+b,total)
    heapq.heappush(array, a+b)

print(total)
