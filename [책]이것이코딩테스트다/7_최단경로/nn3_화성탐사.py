# ##########################################
# ##########################################
# # 3/21복습
# '''
# (0,0) -> (n-1,n-1)까지의 최소거리는?
# n = 125까지라서 다익스트라.

# array[i][j] = i,j 까지 갈때까지 드는 최소비용?
# 보는순서는 상하좌우로 움직이므로 bfs로 봐야겠다.

# '''
# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# for _ in range(int(input())):
#     n = int(input())
    
#     # 1번. 맵정보를 입력받는다.
#     graph = [list(map(int, input().split())) for _ in range(n)]

#     # 2번. distance로 각점까지 걸리는 거리
#     distance = [[INF] * n for _ in range(n)]
#     # 3. 0,0 -> n-1, n-1 시작
#     x, y = 0, 0
#     distance[x][y] = graph[x][y]
#     q = []
#     heapq.heappush(q, (graph[x][y], x, y))
#     while q:
#         # 가장 최단 거리가 짧은 노드에 대해 꺼낸다
#         dist, x, y = heapq.heappop(q)
#         # 현재 노드가 이미 처리된 적이 있다면 무시
#         if distance[x][y] < dist:
#             continue
#         # 현재노드와 연결된 다른 인접한 노드들을 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             cost = dist + graph[x][y]
#             # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧을 경우
#             if cost < distance[nx][ny]:
#                 distance[nx][ny] = cost
#                 heapq.heappush(q, (cost, nx, ny))
#     print(distance[n-1][n-1])



# # import heapq, sys
# # input = sys.stdin.readline
# # INF = int(1e9)
# # dx = [-1,1,0,0]
# # dy = [0,0,-1,1]

# # for _ in range(int(input())):
# #     n = int(input())
# #     # 전체 맵 정보 입력받기
# #     graph = []
# #     for _ in range(n):
# #         graph.append(list(map(int, input().split())))
# #     # 1번. 최단거리 테이블 초기화
# #     distance = [[INF]*n for _ in range(n)]
    
# #     # 시작점 초기화
# #     x, y = 0, 0
# #     distance[x][y] = graph[x][y]
# #     h = []
# #     heapq.heappush(h,(graph[x][y],x,y))
# #     # 2번. 다익스트라 수행
# #     while h:
# #         # 거리가 가장 짧은 노드에 대한 정보 꺼냄.
# #         dist, x, y = heapq.heappop(h)
# #         # 현재 노드가 이미 처리된 적이 있다면
# #         if distance[x][y] < dist: 
# #             continue
# #         # 현재 노드와 연결된 다른 인접한 노드들 확인
# #         for i in range(4):
# #             nx = x + dx[i]
# #             ny = y + dy[i]
# #             if nx < 0 or ny < 0 or nx >= n or ny >= n:
# #                 continue
# #             cost = dist + graph[nx][ny]
            
# #             if cost < distance[nx][ny]:
# #                 distance[nx][ny] = cost
# #                 heapq.heappush(h, (cost,nx,ny))
# #     print(distance[n-1][n-1])

# # ##########################################
# # ##########################################
# # # 내풀이 - 플로이드 => 쓰지말라네? 느리다네.
# # '''
# # 0,0 -> n-1,n-1 인데 각 x,y에 대해서 최단거리를 알아야한다. 매번 구해주면어려움
# # -> 플로이드 사용가능 (n=125이므로 O(125^3))
# # '''
# # INF = int(1e9)

# # for _ in range(int(input())):
# #     n = int(input())
# #     array = [[-1]*(n) for _ in range(n)] # 맵정보를 입력받기 위해
# #     graph = [[INF]*n for _ in range(n)]
    
# #     # 1번. 맵입력받는다.
# #     for i in range(n):
# #         data = list(map(int, input().split()))
# #         for j in range(len(data)):
# #             array[i][j] = data[j]
    
# #     # 2번. 시작점 초기화
# #     graph[0][0] = array[0][0]
    
# #     # 3번.비교시작
# #     dx = [-1,1,0,0]
# #     dy = [0,0,-1,1]
# #     for k in range(n):
# #         for i in range(n):
# #             for j in range(n):
# #                 # 4방향에서 봄
# #                 for z in range(4):
# #                     nx = i + dx[z]
# #                     ny = j + dy[z]
# #                     if nx < 0 or ny < 0 or nx >= n or ny >=n:
# #                         continue
# #                     # min('현재위치까지의 저장된 거리' or '현재위치의 상하좌우 + 현재값')
# #                     graph[i][j] = min(graph[i][j], graph[nx][ny]+array[i][j])
# #     print(graph[n-1][n-1])


