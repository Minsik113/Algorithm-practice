'''
다익스트라 = O(ElogV)
50 x 20만 = 1000만 ok

1/ 연결된도시 카운트세고
2/ 짧은시간부터 쭉 보자.
3/ start -> 각 노드까지 걸리는시간을 distance리스트에 넣는다
4/ distance리스트 값이 INF가 아니라면 count += 1, total_time에더함
5/ print(count, total_time)
(단, 시작도시는 count에서 뺌)
'''

import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split()) # 도시개수, 통로수, 시작노드
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m): # (노드까지, 비용)
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # a->b 비용:C

def dijkstra(start):
    h = []
    distance[start] = 0
    heapq.heappush(h, (0,start)) #(시간, 노드)

    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist: # 이미 본애라면 안봐도됨. 우선순위큐니까
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))

dijkstra(start)
count = 0
total_time = 0
for i in range(len(distance)):
    if distance[i] == INF:
        continue
    count += 1
    total_time = max(total_time, distance[i])
print(count-1, total_time)

