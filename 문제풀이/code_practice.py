'''
start부터 출발해서 최단거리가 k인애들 다 출력해라
없으면 -1

1. BFS로 start부터 각 도시까지 거리 구한다.
2. 거리k인애들 저장한다. (flag = True)
3. 거리가 k+1이 되었을때 반복문 나온다.
4. flag = False라면 그런 도시 없으니 -1 출력

'''
from collections import deque
import sys
input = sys.stdin.readline

n, m, k, start = map(int, input().split())
array = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
# 예외처리
# if k == 0:
#     print(-1)
#     exit()
# 탐색시작 
result = []
flag = False
def bfs(array, visited, start, result):
    global flag
    q = deque()
    t = 0
    q.append((start,t))
    visited[start] = 0
    while q:
        v, time = q.popleft()
        # 찾고자 하는것
        if time == k:
            result.append((v))
            flag = True
        # 더 안봐도 됨
        if time > k:
            break
        for i in array[v]:
            if visited[i] == -1: # 안가본애라면 간다
                q.append((i,time+1))
                visited[i] = time+1
                # 찾는애라면 result에 넣음
                

visited = [-1] * (n+1) # 갈 수 있는 거리를 저장하자
bfs(array, visited, start, result)
# print(visited)
# 답이 존재하지않으면
result.sort()
if not flag:
    print(-1)
else:
    for i in result:
        print(i)

