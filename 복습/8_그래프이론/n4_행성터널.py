##########################################
##########################################
# 3/22 - 시간초과남. 다시.

##########################################
##########################################
#
'''
행성끼리 연결하려함.
행성위치 = 3차원좌표
-> (AB행성거리,A,B)로 리스트 새로 만든다.
짧은거리끼리 이어서 전체 연결되게한다. 
최소비용은?
-> 크루스칼이용

크루스칼은 맞는데 N = 10^5라서 거리비교할때 O(N(N-1)/2)이면 시간초과남 
-> 이걸 줄여야 이용가능함.
-> x,y,z를 각각 보면서 비교 3x(N-1)의 간선을 만들어서 크루스칼하면
O(3Nlog3N)으로 시간안에됨.

'''

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# n = int(input())

# # 부모초기화
# parent = [0] * (n+1)
# for i in range(1,n+1):
#     parent[i] = i

# x = []
# y = []
# z = []
# for i in range(n):
#     pos3d = list(map(int, input().split()))
#     x.append((pos3d[0],i))
#     y.append((pos3d[1],i))
#     z.append((pos3d[2],i))
# x.sort()
# y.sort()
# z.sort()

# edges = [] # 여기에 변환한 도로상황 넣음
# # 인접한 도시들로부터 간선 정보를 추출하자
# for i in range(n-1): # (AB도시거리,A,B)
#     edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
#     edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
#     edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

# # 길이 짧은순으로 sort
# edges.sort()
# result = 0
# for edge in edges:
#     cost, a, b = edge

#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
    
# print(result)