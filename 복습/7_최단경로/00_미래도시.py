'''
1번 도시출발. k도시를 거쳐서 x도시로간다.
(1번 -> k번 -> x번)

1. 다익스트라 사용 O(ElogV)
2. 플로이드워셜 사용 O(N^3)
-> N=10^2 이므로
'''

########################################
########################################
# 다익스트라
# import sys, heapq
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# distance = [INF] * (n+1)

# for _ in range(m): # (노드,비용)
#     a, b = map(int, input().split()) # a->b 까지 비용 1
#     graph[a].append((b,1))
#     graph[b].append((a,1))

# x, k = map(int, input().split())

# def dijkstra(start):
#     h = []
#     heapq.heappush(h, (0, start)) # (비용, 노드)
#     distance[start] = 0
#     while h:
#         dist, now = heapq.heappop(h)
#         if dist > distance[now]: # 볼필요가없음
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if distance[i[0]] > cost:
#                 distance[i[0]] = cost
#                 heapq.heappush(h, (cost, i[0]))

# # 1~k 가자
# dijkstra(1)
# total_time = 0
# # print(distance)    
# if distance[k] == INF: # 못가는 곳이라면 -1출력
#     print(-1)
#     exit()
# else:
#     total_time = distance[k]
# # k~x가자
# distance = [INF] * (n+1)
# dijkstra(k)
# # print(distance)    
# if distance[x] == INF: # 못가는 곳이라면 -1출력
#     print(-1)
#     exit()
# else:
#     total_time += distance[x]

# print(total_time)

########################################
########################################
# 플로이드워셜
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [ [INF]*(n+1) for _ in range(n+1)]

# 자기자신 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        graph[a][b] = 0
# 간선 정보 입력받고 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# 최종도시, 거쳐야하는도시
x, k = map(int, input().split())
# 점화식에따라 진행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

value = graph[1][k]+ graph[k][x]
if value >= INF:
    print(-1)
else:
    print(value)

