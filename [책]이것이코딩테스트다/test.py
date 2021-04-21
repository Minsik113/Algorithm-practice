import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split()) # 1->k -> x

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
total_time = 0
if distance[k] == INF:
    print(-1)
    exit()
else:
    total_time += distance[k]

distance = [INF] * (n+1)
dijkstra(k)
if distance[x] == INF:
    print(-1)
    exit()
else:
    total_time += distance[x]
print(total_time)