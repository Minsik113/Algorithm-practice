import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = int(input())
start = int(input())
# 맵 입력받음
graph = [[] for _ in range(n+1)]
# 방문체크
visited = [False] * (n+1)
# 최단거리 테이블
distance = [INF] * (n+1)

# 모든 간선 정보 입력받자
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start)) # 비용, 시작노드
    distance[start] = 0

    while h:
        dist, now = heapq.heappop(h)
        # 예외처리
        if distance[now] < dist: # 이미 처리된적 있는노드라면 넘어감
            continue # heapq로 보는거니까 먼저처리됏으면 더 작은값임
        for i in graph[now]:
            cost = dist + i[1]
            # 현재노드를 거쳐서 다른노드를 가는경우가 더 작다면 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush((h, (cost, i[0])))


dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])