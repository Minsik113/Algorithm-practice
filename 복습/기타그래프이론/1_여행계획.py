'''
전체 도시에 대해 union find해서 
여행 도시들이 모두 같은 집합인지 체크하면된다.

'''
########################################
########################################
# 좀더 깔끔한 코드
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

# 부모 초기화
for i in range(1, n+1):
    parent[i] = i

# 도로상황 입력받기
for i in range(n):
    chart = list(map(int, input().split()))
    for j in range(n):
        if chart[j] == 1:
            union_parent(parent, i, j)

array = list(map(int, input().split()))

result = True
for i in range(m-1):
    if find_parent(parent, array[i]) != find_parent(parent, array[i+1]):
        result = False
        break

if result:
    print("YES")
else:
    print("NO")
########################################
########################################
# 내풀이
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

# n, m = map(int, input().split())
# parent = [0] * (n+1)
# chart = []

# # 부모 초기화
# for i in range(1, n+1):
#     parent[i] = i

# # 도로상황 입력받기
# for i in range(n):
#     chart.append(list(map(int, input().split())))

# # chart[a][b] == 1이면 a와 b의 부모 같게한다.
# for i in range(n):
#     for j in range(i,n):
#         if chart[i][j] == 1:
#             union_parent(parent, i, j)

# array = list(map(int, input().split()))

# check = True
# start = find_parent(parent, array[0])
# for i in range(1, len(array)):
#     go = find_parent(parent, array[i])
#     if start != go:
#         check = False
#         break
# if check:
#     print("YES")
# else:
#     print("NO")