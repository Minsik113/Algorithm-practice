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