'''
1. N개의 강의
2. N개의줄에 강의시간, 선수과목 수 나옴

선수과목 -> 위상정렬
각 과목이 끝나는 시간을 출력해라.

위상정렬 x 과목수 = O( V(V+E) )
'''
from collections import deque 
import copy

n = int(input())
indegree = [0] * (n+1) # 1~n
graph = [[] for _ in range(n+1) ] # 1~n
time = [0] * (n+1) # 각 과목당 걸리는 시간 측정. 변할 수 있음

for i in range(1, n+1): # (시간,선수과목들)
    save = list(map(int,input().split()))
    time[i] = save[0]
    for j in save[1:-1]: # index=1부터 -1값전까지.
        indegree[i] += 1
        graph[j].append(i)

# 1번. indegree = 0인것을 queue에 넣는다.
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i) # (과목, 소요시간)

    #2번
    while q:
        now = q.popleft() #(과목, 소요시간)
        # 2번 a
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            # 2번 b
            if indegree[i] == 0:
                q.append(i)
    
    # 위상정렬 결과 출력
    for i in range(1, n+1):
        print(result[i])

topology_sort()
# 과목 오름차순으로 (과목번호, 걸리는시간)


########################################
########################################
# 내풀이
# from collections import deque 

# n = int(input())
# indegree = [0] * (n+1) # 1~n
# graph = [[] for _ in range(n+1) ] # 1~n
# time = [0] * (n+1) # 각 과목당 걸리는 시간 측정. 변할 수 있음

# for i in range(1, n+1): # (시간,선수과목들)
#     save = list(map(int,input().split()))
#     time[i] = save[0]
#     for j in range(1, len(save)):
#         if save[j] == -1:
#             break
#         graph[save[j]].append(i)
#         indegree[i] += 1

# # 1번. indegree = 0인것을 queue에 넣는다.
# result = []
# def topology_sort():
#     q = deque()
#     for i in range(1, n+1):
#         if indegree[i] == 0:
#             q.append((i,time[i])) # (과목, 소요시간)

#     #2번
#     while q:
#         now, temp = q.popleft() #(과목, 소요시간)
#         result.append((now,temp))
#         # 2번 a
#         for i in graph[now]:
#             indegree[i] -= 1
#             # 2번 b
#             if indegree[i] == 0:
#                 q.append((i,temp+time[i]))

# topology_sort()
# # 과목 오름차순으로 (과목번호, 걸리는시간)
# result.sort()
# for i in result:
#     print(i[1])


