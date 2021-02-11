'''
1/20
문제 난이도: Gold 4
문제 유형: 이진 탐색
추천 풀이 시간: 60분
내용: 공장 ~ 공장까지 가는 길들에 무게제한이 있다.
 물건을 옮길때 무게를 최대로 싣고 갈 수 있는 길이 있다.
 그 최대무게는?
'''
# 다리 개수 100,000 중량제한 1,000,000,000
# log나 루트를 씌워줄만한 껀덕지가 있지않을까.
# 찾고자 하는 값에 대해 이진탐색을 해야함.(중량에 이진탐색을 한다.)
# BFS를 이용해서 a -> b로 이동
# 간선의 개수 m만큼 시간이 걸림. O(m)
# O(M * logC)하면 약 300만이 걸림. 금방이네.

# 일단 공장하나의 최소중량 최대중량을 정해서 그거로 start end놓고 이진탐색

######################  ######################
# 나동빈
from collections import deque

n, m = map(int, input().split(' '))
adj = [[] for _ in range(n+1)]

def bfs(c):
    queue = deque([start_node]) # deque = [start]
    visited = [False] * (n+1)
    visited[start_node] = True

    while queue:
        x = queue.popleft() # 시작노드를 queue에서 제거
        for y, weight in adj[x]:
            if not visited[y] and weight >= c: # 안 가봤고, c무게보다 크다면
                visited[y] = True
                queue.append(y)
    return visited[end_node]

start = 1000000000
end = 1

for _ in range(m):
    x, y, weight = map(int, input().split(' '))
    adj[x].append((y,weight))
    adj[y].append((x,weight))
    start = min(start, weight)
    end = max(end, weight)

start_node, end_node = map(int, input().split(' '))

result = start
while (start <= end):
    mid = (start + end) // 2 # mid는 현재 중량을 의미
    if bfs(mid): # 이동 가능하므로, 중량을 증가시킴
        result = mid
        start = mid + 1
    else: # 이동 불가능하므로, 중량을 감소시킴
        end = mid - 1

print(result)