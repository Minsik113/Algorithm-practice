##########################################
##########################################
# 
# import sys
# input = sys.stdin.readline

# INF = int(1e9)

# n, m = map(int, input().split())
# graph = [[INF] * (n+1) for _ in range(n+1)]

# # 자기자신은 갈 수 있으므로 0 으로초기화
# for i in range(1, n+1):
#     graph[i][i] = 0


# # a-b가 연결되어있으므로 입력받는다.
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1

# # 플로이드워셜 수행
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# result = 0
# for i in range(1, n+1):
#     count = 0
#     for j in range(1, n+1):
#         if graph[i][j] != INF or graph[j][i] != INF:
#             count += 1
#     if count == n: # 연결이 되어있기에 정확한 순서를 정할 수 있다는 거니까
#         result += 1
# print(result)