##########################################
##########################################
# 3/11복습 어려운듯,
'''
위상정렬 문제이다.

edges[a].append(~~)
indegree[a] 
indegree 0 인거부터 쭉보면서 최소걸리는시간구하며될듯?

'''

from collections import deque

n = int(input())

# 1번. 차수 세기위해 선언
indegree = [0] * (n+1)
# 2번. 연결관계 저장하기 위해 선언
graph = [[] for _ in range(n+1)]

# 3번. 맵 입력받는다
time_list = [0] # 시간정보 입력
for i in range(1, n+1):
    data = list(map(int, input().split()))
    time_list.append(data[0])
    data = data[1:-1] # 비용과,-1은 뺀다.
    for j in data:
        graph[j].append(i) # j들을 다 수행해야 i를 들을 수 있다.
        indegree[i] += 1 # j들을 다 수행해야 i를 들을 수 있다.

# print(graph)
# print(indegree)

# 4번. 진입차수 0인것을 queue에 넣는다
q = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i) # i번째 과목을 듣자.

while q:
    now = q.popleft()
    
    for i in graph[now]: # 연결된애들 보자
        indegree[i] -= 1
        if indegree[i] == 0: # 
            q.append(i)
            time_list[i] = max(time_list[i], time_list[now]+time_list[i])

for i in range(1, n+1):
    print(time_list[i])
##########################################
##########################################
# 
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


