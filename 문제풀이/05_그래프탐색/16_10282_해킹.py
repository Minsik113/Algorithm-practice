'''
# 1/29
# 문제 난이도: Gold 4
# 문제 유형: dijkstra 최단경로
# 추천 풀이 시간: 50분
'''
'''
최소시간 or 최소 거리 이런거 구할때는 다익스트라 활용하는 문제구나~생각.
dijkstra는 '우선순위 큐'도 다룰 수 있어야 함.
정점의 개수N(10,000), 간선의개수D(100,000)
우선순위 큐를 사용하여 O(NlogD)
'''

import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0,start))
    distance[start] = 0 # 다른애들은 INF로 초기화 되어있다.
    
    while heap_data:
        dist, now = heapq.heappop(heap_data) # dist, now = (cost, x )
        if distance[now] < dist:
            continue
        for i in array[now]: # array = (x, cost)
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))

for _ in range(int(input())):a
    n, m, start = map(int, input().split())
    array = [[] for i in range(n+1)]
    distance = [1e9] * (n+1)

    # array = (점, cost)
    for i in range(m):
        x, y, cost = map(int, input().split())
        array[y].append((x,cost))

    dijkstra(start)
    # distance에 저장되어있다.
    count = 0  # 몇 개의 컴퓨터 연결되어있는가.
    max_distance = 0
    for i in distance:
        if i != 1e9:
            count += 1
            if i > max_distance:
                max_distance = i
    print(count, max_distance)

################  ################
# 나동빈
import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
    heap_data = [] 
    heapq.heappush(heap_data, (0,start))
    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data) # 가중치, 현재노드
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1] # (노드,가중치)니까 [1] = cost
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data,(cost,i[0]))

for _ in range(int(input())):
    n, m, start = map(int,input().split())
    adj = [[] for i in range(n+1)]
    distance = [1e9] * (n+1) # 10^9 = INF

    for _ in range(m):
        x, y, cost = map(int,input().split())
        adj[y].append((x,cost))
    
    dijkstra(start)
    count = 0
    max_distance = 0
    for i in distance:
        if i != 1e9:
            count += 1
            if i > max_distance:
                max_distance = i
    print(count, max_distance)