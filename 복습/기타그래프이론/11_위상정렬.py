from collections import deque

v, e = map(int, input().split())
# 모든 노드의 진입차수 0으로 초기화
indegree = [0] * (v+1)
# 간선정보 담자
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # a -> b 니까 b의 indegree를 증가시킴
    indegree[b] += 1
print(graph)
print(indegree)
exit()
# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()
    # 1번 진입차수가 0 인걸 queue에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    # 2번
    while q:
        now = q.popleft()
        result.append(now)
        # 2번 a
        for i in graph[now]:
            indegree[i] -= 1
            # 2번 b
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')

topology_sort()

