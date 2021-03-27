'''
지금까지 말한 수 중 중간값을 말한다.

if 개수가 짝수라면) 두 수중 작은수를 출력.
-> 우선순위 큐를 이용해서 계속넣는다.
# 짝수개라면 h[len(h) // 2 - 1]
if len(h) % 2 == 0: 
# 홀수개라면 h[len(h)//2]

'''
'''
바로바로 정렬어떻게하지? 
-> 1~n길이까지 매번 정렬해주는건 너무 길다.

insert로 위치찾아서 삽입을할까? 그러면
매번 O(n)이니까

'''
import sys, heapq
input = sys.stdin.readline

n = int(input())
q = []
length = 0
result = []

for i in range(n):
    x = int(input())
    heapq.heappush(q, x)
    length += 1
    if length % 2 == 0:
        # print(h[length//2 - 1])
        result.append(q[length//2 - 1])
    else:
        # print(h[length//2])
        result.append(q[length//2])
print(q)
print(result)