'''
O(V^2)
O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야하고, 
현재 노드와 연결된 노드를 매번 일일이 확인해야함
-> 리스트를 하나씩 찾아보는것을 줄여보자
=> 우선순위 큐를 이용하면 빠르겠네.
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 담자. 
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 리스트
visited = [False] * (n+1)
# 최단거리 테이블 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받자
for _ in range(m):
    a, b, c = map(int, input().split())
    # a ~> b 까지 이동하는데 비용 c
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    # start로부터 당장 도달가능한 노드들을 본다.
    for j in graph[start]: # distance[a] = (b,c)
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1] # (기존비용, 현재까지거리 + 연결된 거리값)
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
            
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, INFINITY 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


