'''
1 -> v1 -> v2 -> n
다익스트라 3번쓰면됨

'''
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

# 1. 연결관계 입력
graph = [[] for _ in range(n+1)]
for _ in range(e): # 무방향
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # 노드, cost
    graph[b].append((a,c))

v1, v2 = map(int, input().split())
# 거리
def dijkstra(start, x):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance[x]

min_value = 0    
# 3번의 다익스트라
result = [1,v1,v2,n]
pre = result[0]
flag = True
for k in range(1, len(result)):
    distance = [INF] * (n+1)
    min_value += dijkstra(pre, result[k])
    pre = result[k]
    
if min_value >= INF:
    print(-1)
else:
    print(min_value)
