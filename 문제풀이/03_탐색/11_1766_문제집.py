'''
# 1/22
# 문제 난이도: Gold 2
# 문제 유형: 힙, 위상 정렬
# 추천 풀이 시간: 40분
'''
# 리스트로 연결을 해놔야 한다는 의미
'''
1/ N개의 문제는 모두 풀어야 한다.
2/ 먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 
    좋은 문제를 반드시 먼저 풀어야 한다.
3/ 가능하면 쉬운 문제부터 풀어야 한다.
'''
import heapq

n, m = map(int, input().split()) # n개의문제 , m개의순서

check = [[] for i in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    check[a].append(b)
    indegree[b] += 1

heap = []
for i in range(1, n+1):
    if indegree[i] == 0: # 선수과목이 없다면 큐에넣는다.
        heapq.heappush(heap, i)

result = []
while heap: # queue 빌때까지 본다.
    x = heapq.heappop(heap) # queue에 있는애들중 가장 중요한거 먼저 출력.
    result.append(x)

    for i in check[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)

for i in result:
    print(i, end=' ')

