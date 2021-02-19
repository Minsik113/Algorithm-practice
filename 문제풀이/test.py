import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # (노드, 거리)

def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start)) # (거리, 노드)
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)
        if dist > distance[now]: # 비교대상이 아니면 건너뛴다.
            continue
        # 현재노드와 인접한 노드들을 볼것이다.
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost,i[0]))

dijkstra(start)
print(distance)