# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(start):
#     q = deque()
#     q.append(start)
#     visited[start] = 1
#     while q:
#         x = q.popleft()
#         for i in graph[x]:
#             # 아직 방문을 안한곳이라면
#             if visited[i] == 0:
#                 visited[i] = -visited[x]
#                 q.append(i)
#             # 방문한곳-> 현재와 같은지 봐야함
#             else:
#                 if visited[i] == visited[x]:
#                     return False
#     return True

# test_case = int(input())
# for _ in range(test_case):
#     v, e = map(int, input().split())
#     graph = [[] for _ in range(v+1)]
#     for _ in range(e):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
    
#     visited = [0] * (v+1)
#     flag = True
#     for i in range(1, v+1):
#         if visited[i] == 0:
#             if not bfs(i):
#                 flag = False
#                 break
#     print("YES" if flag else "NO")


# # import sys
# # from collections import deque
# # input = sys.stdin.readline

# # def bfs(start):
# #     visited[start] = 1
# #     q = deque()
# #     q.append(start)
# #     while q:
# #         x = q.popleft()
# #         for k in graph[x]:
# #             if visited[k] == 0:
# #                 visited[k] = -visited[x]
# #                 q.append(k)
# #             else:
# #                 if visited[k] == visited[x]:
# #                     return False
# #     return True

# # for _ in range(int(input())):
# #     v, e = map(int, input().split())
    
# #     visited = [0 for _ in range(v+1)] # 모든변이 이어져있는지 체크
# #     graph = [[] for _ in range(v+1)] # 연결관계
# #     for _ in range(e):
# #         a, b = map(int, input().split())
# #         graph[a].append(b)
# #         graph[b].append(a)
    
# #     flag = True
# #     for i in range(1, v+1):
# #         if visited[i] == 0:
# #             if not bfs(i):
# #                 flag = False
# #                 break
# #     print(visited)
# #     print("YES" if flag else "NO")
