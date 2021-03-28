'''
직관적으로 전체 과정은 E개의 원소를 우선순위큐에 
넣었다가 모두 빼내는 연산과 매우 유사하다.
시간복잡도 O(ElogE)
-> 중복 간선을 포함하지 않는 경우 O(ElogV)로 정리할 수 있다.

n:정점수 m:연결관계수
다익스트라:O(m)
플로이드워셜:
한점에서 -> 다른모든점 최단거리 : 다익스트라를 n번?

'''
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input()) # 시작점

# 거리 선언 및 초기화
distance = [INF] * (v+1)

# 연결관계 입력받자. 길이 여러개일 수 있다.
# -> 다 입력받고 거리비교할떄 다시보자
edges = [[] for _ in range(v+1)] 
for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append((b,c)) # a->b cost

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in edges[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# def dijkstra(start):
#     q = []
#     distance[start] = 0
#     heapq.heappush(q, (0, start)) # 거리, a까지
#     while q:
#         cost, a = heapq.heappop(q)
#         if distance[a] < cost: # 이미 더 짧은애로 바꿧으니 볼 필요없다
#             continue
#         # 더 짧은거리가 들어왔으니 얘를 통해 바꿔야 할 애들이 있는지 본다
#         for i in edges[a]: # a-> @로 가는애들
#             if distance[i[0]] > cost + i[1]: # 저장된거리 > 바뀌었을떄거리
#                 distance[i[0]] = cost + i[1]
#                 heapq.heappush(q, (cost+i[1], i[0]))

dijkstra(start)
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])