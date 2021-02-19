'''
O(ElogV)
'''
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드개수, 간선개수
n, m = map(int, input().split())
# 시작 노드 
start = int(input())
# 각 노드끼리의 연결관계 담을 리스트
graph = [ [] for _ in range(n+1)]
# 최단거리 테이블 초기화
distnace = [INF] * (n+1)

# 1. 모든 간선정보 입력받는다
for _ in range(m):
    a, b, c= map(int, input().split())
    graph[a].append((b,c)) # a ~> b . 비용: c

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해서, 큐에 삽입
    q = heapq.heappush(q, (0,start)) # (거리, 시작노드)
    distnace[start] = 0
    while q:
        dist, now = heapq.heappop(q) # (거리, 시작노드)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]: # (b,c) = now~>b . 비용 = c
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distnace[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
                print(cost)

dijkstra(start)
print(distnace)
exit()
for i in range(1, n+1):
    if distnace[i] == INF:
        print("INFINITY")
    else:
        print(distnace[i])





dijkstra(start)

