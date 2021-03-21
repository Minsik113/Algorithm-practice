##########################################
##########################################
# 3/21 복습. 
# '''
# 정확히 자기 위치를 알 수 있는가
#  -> 모든점에서 모든점까지의 거리
# ex)
# 5개 점이있음
# a 점에서 b,c,d,e까지의 거리가 INF가 아니라면 순서비교가 가능하다는뜻
# [i][j] 와 [j][i] 중 inf가없다면 count 증가시켜본다.
# -> 플로이드워셜 ㄱ

# '''
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())

# # 각 노드의 관계 입력받자
# distance = [[INF] * (n+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     distance[i][i] = 0

# for _ in range(m):
#     a, b = map(int, input().split()) # a를해야 b할수있다. b할라면 a를해야함
#     distance[a][b] = 1

# # 플로이드워셜 시행
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

# # 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크한다
# result = 0
# for i in range(1, n+1):
#     count = 0
#     for j in range(1, n+1):
#         if distance[i][j] != INF or distance[j][i] != INF:
#             count += 1
#     if count == n:
#         result += 1
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(distance[i][j], end=' ')
#     print()
# print(result)