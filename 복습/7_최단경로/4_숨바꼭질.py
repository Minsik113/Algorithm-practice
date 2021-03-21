##########################################
##########################################
# 3/21 복습. bfs로 풀어봄
'''
가장 먼 헛간 찾아라
1에서 제일먼 노드

-> bfs로 접근하면됨

'''
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

# 맵입력받음
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # a->b
    graph[b].append(a)

visited = [False] * (n+1)
count = [0] * (n+1)
def bfs(start, count, visited):
    q = deque()
    q.append((0, start))
    visited[start] = True
    count[start] = 0
    while q:
        dist, now = q.popleft()
        for v in graph[now]:
            if not visited[v]:
                q.append((dist+1, v))
                count[v] = dist+1
                visited[v] = True

bfs(1,count,visited)
number = 0
max_value = max(count)
same_number = count.count(max_value)
for i in range(1, n+1):
    if max_value == count[i]:
        number = i
        break
print(number, max_value, same_number)


'''
마지막에 나는 일차 for문을 2번 사용해서 답을 구했고,
다른 풀이는 for문을 1번 사용해서 답을 구했다.
'''
### # distnace까지 구했다고 가정하고 해보자
# max_value = 0
# result = []
# pos = 0
# for i in range(1, n+1):
#     # 더 큰 수가 나오면 갱신해준다.
#     if max_value < distance[i]:
#         max_value = distance[i]
#         pos = i
#         result = []
#         result.append(i)
#     # 같은수나오면 추가해줌        
#     elif max_value == distance[i]: 
#         result.append(i)
# print(count, pos, len(result))

##########################################
##########################################
# 내풀이
'''
1번헛간 -> 제일거리가 먼 헛간 출력
다익스트라로 distance테이블 보면 끝

'''
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
# 1번. 연결된 맵 정보를 저장할 리스트 생선한다
graph = [[] for _ in range(n+1)]
# 2번. 최단거리 저장할 리스트 생성
distnace = [INF] * (n+1)

# 3번. 맵정보 입력받음
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1)) # a<->b 비용1
    graph[b].append((a,1))

# 4번. 다익스트라 시작
def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start)) # (노드까지거리, 노드)
    distnace[start] = 0

    while h:
        dist, now = heapq.heappop(h)
        if distnace[now] < dist: # 볼필요 없음. now 지나는 것보다 더 빠른길이 있다.
            continue
        for i in graph[now]: # 연결된애들의 거리 갱신할거 있는지 보자
            cost = dist + i[1]
            if cost < distnace[i[0]]: # 더 작다면 갱신한다
                distnace[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))

dijkstra(1)

# 5번. distance테이블보자. 제일 거리먼것 찾아내자
max_value = 0
pos = -1
for i in range(1, n+1):
    if max_value < distnace[i]:
        max_value = distnace[i]
        pos = i
# 6번. 같은거리를 가진 애들이 있는지 체크하자
count = 0
for i in range(1, n+1):
    if distnace[i] == max_value:
        count += 1
print(distnace)        
print(pos, max_value, count)