'''
nxm 

다리 조건
1. 직선 (가로or세로)
2. 길이가 2이상

각점에서 가능한 섬까지의 거리를구하자
-> edges[(섬1-섬2거리, 섬1,섬2)]
heapq로 짧은애들끼리해서 unionfind하면될듯?
'''
import heapq, sys
from collections import deque
input = sys.stdin.readline

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def bfs(serial_number, x, y):
    q = deque()
    q.append((x,y))
    array[x][y] = serial_number
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or array[nx][ny] != 1:
                continue
            # array[nx][ny] == 1인곳
            array[nx][ny] = serial_number
            q.append((nx, ny))

# 2이상의 숫자로 이루어지면 섬이다.
# 가까운거리의 섬까지의 거리를 저장한다.
def find_island(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or array[nx][ny] != 0:
            continue
        # k방향에 바다(0)가 있음.
        count = 1
        zx, zy = nx, ny
        while True:
            zx += dx[k]
            zy += dy[k]
            if zx < 0 or zy < 0 or zx >= n or zy >= m:
                break
            # 범위 안에 있음 -> 섬 / 바다 
            # 1. 바다라면 계속간다
            if array[zx][zy] == 0:
                count += 1
            # 2. 자신과 다른 섬이라면 갯수세고 다른방향본다
            elif array[zx][zy] != array[nx][ny] and array[zx][zy] >= 2:
                if count >= 2:
                    heapq.heappush(edges, (count, array[zx][zy], array[x][y]))
                break

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 1.맵을 내입맛에 따라 변환하자
dx = [-1,1,0,0]
dy = [0,0,-1,1]

serial_number = 2
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            bfs(serial_number, i, j)
            serial_number += 1

edges = []
for i in range(n):
    for j in range(m):
        if array[i][j] >= 2:
            find_island(i,j)

# 부모 선언 및 초기화
parent = [0] * (serial_number)
for i in range(serial_number):
    parent[i] = i
# 거리
result = 0
while edges:
    cost, v1, v2 = heapq.heappop(edges)
    if find_parent(parent, v1) != find_parent(parent, v2):
        union_parent(parent, v1, v2)
        result += cost
        # print(cost, v1, v2)

# 모든 섬이 연결되었는지 체크 = 2~serialnumber-1까지
if serial_number >= 2:
    flag = True
    save = []
    pre = find_parent(parent, 2)
    for i in range(3, serial_number):
        if pre != find_parent(parent, i):
            flag = False
            break
    print(result if flag else -1)
else:
    print(-1)