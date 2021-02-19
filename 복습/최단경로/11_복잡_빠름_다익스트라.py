'''
O(ElogV)
노드를 하나씩 꺼내 검사하는 반복문(while)은 
노드의 개수 V이상의 횟수로 처리되지 않는다.
-> heapq에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수는 
최대 간선의 개수(E)만큼 연산이 수행될 수 있다.

##
직관적으로 전체 과정은 E개의 원소를 우선순위큐에 
넣었다가 모두 빼내는 연산과 매우 유사하다.
시간복잡도 O(ElogE)
-> 중복 간선을 포함하지 않는 경우 O(ElogV)로 정리할 수 있다.
 (O(ElogE) -> O(ElogV^2) -> O(2ElogV) -> O(ElogV))
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
distance = [INF] * (n+1)

# 1. 모든 간선정보 입력받는다
for _ in range(m):
    a, b, c= map(int, input().split())
    graph[a].append((b,c)) # (노드, 거리)

def dijkstra(start):
    h = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해서, 큐에 삽입
    heapq.heappush(h, (0,start)) # (거리, 시작노드)
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h) # (거리, 시작노드)
        # 이미 거리가 더 짧은 길이 있으므로 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]: # (b,c) = now~>b . 비용 = c
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost,i[0]))
                print(cost)

dijkstra(start)
print(distance)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
