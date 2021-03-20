import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

# 맵 입력받는다
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 최단거리테이블 초기화
distance = [INF] * (v+1)
start = int(input())

def dijkstra(start):
    distance[start] = 0
    h = []
    heapq.heappush(h, (0, start)) # 거리와 노드
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost,i[0]))

dijkstra(start)
# 시작(3) -> 5
print(distance[5])
# 시작(3) -> 모든점
for i in range(1, v+1):
    print(distance[i])