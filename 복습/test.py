'''
탑승구에 비행기 넣기
'''

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

g = int(input()) # 탑승구 수
p = int(input()) # 비행기 수

planes = [int(input()) for _ in range(p)]

# 대표값 초기화
# visited = [False] * (g+1)
parent = [0] * (g+1) # i번째 공항아래로 댈 수 있는 비행기 수
for i in range(1, g+1):
    parent[i] = i 

# 비행기 넣어보자
count = 0
for plane in planes:
    # 공항의 max값보다 번호 큰 비행기가 들어오면 맨 끝쪽에
    check = find_parent(parent, plane)
    if check == 0: # 현재 루트가 0이라면
        break
    union_parent(parent, check, check-1)
    count += 1
print(count)