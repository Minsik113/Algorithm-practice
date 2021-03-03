
'''
start부터 출발해서 최단거리가 k인애들 다 출력해라
없으면 -1

1. BFS로 start부터 각 도시까지 거리 구한다.
2. 거리k인애들 저장한다. (flag = True)
3. 거리가 k+1이 되었을때 반복문 나온다.
4. flag = False라면 그런 도시 없으니 -1 출력
'''
##########################################
##########################################
# 3/3 복습
from collections import deque
import sys
input = sys.stdin.readline

n, m, k, start = map(int, input().split())
array = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
# 예외처리
# if k == 0:
#     print(-1)
#     exit()
# 탐색시작 
result = []
flag = False
def bfs(array, visited, start, result):
    global flag
    q = deque()
    t = 0
    q.append((start,t))
    visited[start] = 0
    while q:
        v, time = q.popleft()
        # 찾고자 하는것
        if time == k:
            result.append((v))
            flag = True
        # 더 안봐도 됨
        if time > k:
            break
        for i in array[v]:
            if visited[i] == -1: # 안가본애라면 간다
                q.append((i,time+1))
                visited[i] = time+1
                # 찾는애라면 result에 넣음

visited = [-1] * (n+1) # 갈 수 있는 거리를 저장하자
bfs(array, visited, start, result)
# 답이 존재하지않으면
result.sort()
if not flag:
    print(-1)
else:
    for i in result:
        print(i)
##########################################
##########################################
# 다시품
'''
bfs dfs의 시간복잡도
V:정점 E:간선 수
인접리스트 : O(V+E)
인접행렬:O(V*2)

n, m, k, start_node
n개의 도시. 
m개의 도로
최단거리가 k인 모든도시를 오름차순출력
-> bfs로 level 가져가기.
-> O(30만 + 100만)

-> level == k 라면 그때 출력 level > k면 break
'''
# from collections import deque

# # 도시개수, 도로개수, 찾는거리값, 시작도시
# n, m, k, start = map(int, input().split())
# graph = [[] for i in range(n+1)] # 1~n
# # 맵 입력
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# # 거리찾기
# visited = [False] * (n+1)
# result = []
# def bfs(graph, start, visited):
#     global result
#     q = deque()
#     q.append((0,start))
#     visited[start] = True
#     while q:
#         level, v = q.popleft()
#         if level == k:
#             result.append(v)
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 q.append((level+1,i))

# bfs(graph, start, visited)
# result.sort()
# if len(result) == 0:
#     print(-1)
# for i in result:
#     print(i)
##########################################
##########################################
# 내풀이 - queue에 (도시,level) 넣음
# from collections import deque

# n, m, k, x = map(int, input().split())
# array = [[] for i in range(n+1)] # 1~n까지의 연결리스트 생성
# for i in range(m):
#     a, b = map(int, input().split())
#     array[a].append(b)

# visited = [False] * (n+1)
# result = []
# def bfs(start):
#     q = deque()
#     q.append((start,0))
#     visited[start] = True
#     while q:
#         vv = q.popleft()
#         v, level = vv[0], vv[1]
#         if level == k:
#             result.append(v)
#         for i in array[v]:
#             if not visited[i]:
#                 q.append((i,level+1))
#                 visited[i] = True

# bfs(x)
# if result:
#     result.sort()
#     for i in result:
#         print(i)
# else:
#     print(-1)

##########################################
##########################################
# 각 도시마다 최단거리 설정
# from collections import deque

# n, m, k, x = map(int, input().split())
# array = [[] for i in range(n+1)] # 1~n까지의 연결리스트 생성
# for i in range(m):
#     a, b = map(int, input().split())
#     array[a].append(b)
# # 모든 도시 거리 초기화
# distance = [-1] * (n+1)
# distance[x] = 0

# def bfs(start):
#     q = deque()
#     q.append(start)
#     while q:
#         now = q.popleft()
#         for i in array[now]:
#             #아직 방문하지 않았다면
#             if distance[i] == -1:
#                 # 최단거리 갱신
#                 distance[i] = distance[now] + 1
#                 q.append(i)
# bfs(x)
# check = False
# for i in range(1, n+1):
#     if distance[i] == k:
#         print(i)
#         check = True
# # 최단 도시 없다면 -1
# if check == False:
#     print(-1)


    

