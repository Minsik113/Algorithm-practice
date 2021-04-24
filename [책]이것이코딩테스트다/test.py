import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a, b, w = list(map(int, input().split()))
    graph[a].append((b, w)) # a->b w

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # (거리, 노드)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 처리된 적이 있다,
            continue 
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))

result = 0
dijkstra(start)
if distance[3] == INF: # 시작노드->3 까지 거리
    print(-1)
    exit()
result += distance[3]
distane = [INF for _ in range(n)]
dijkstra(3)
if distance[7] == INF:
    print(-1)
    exit()
result += distance[7]
print(result)