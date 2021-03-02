'''
1. bfs로 바이러스 증식.
-> 번호가 낮은것부터 증식해야함. heapq?
2. s초가 지난 후 (x,y)에있는 바이러스 번호찾기
3. (x,y)가 오염되지 않았다면 0 출력
'''
import heapq
from collections import deque

n, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
s, fx, fy = map(int,input().split()) 

h = []
# 시작위치찾는데 200*200 = 4만
max_virus = 0
for i in range(n):
    for j in range(n):
        if array[i][j] != 0:
            h.append((array[i][j],i,j,0))
            max_virus = max(max_virus, array[i][j])
h = sorted(h, key=lambda x:x[0]) # virus 기준으로 오름차순정렬
# 정렬된 리스트 -> deque()로
qq = deque()
for i in h:
    qq.append(i)

def bfs(array, qq):
    global max_virus, result
    while qq:
        virus, x, y, time = qq.popleft()
        # 바이러스 퍼트리기 전에 확인한다.
        if time == s:
            return
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if array[nx][ny] == 0:
                array[nx][ny] = virus
                qq.append((virus,nx,ny,time+1))
                
# 바이러스 순서대로 bfs진행
result = 0
bfs(array, qq)
# print(array)
print(array[fx-1][fy-1])

