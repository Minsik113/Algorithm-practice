'''
Union 연산이 편향되게 이루어지는 경우 Find함수가 비효율적으로 동작한다.
최악의 경우, Find함수가 모든 노드를 다 확인하게 되어 O(V)된다.
(선형적으로 나란히 연결되었을 때)
=> 경로 압축(Path compression)을 이용한다.
'''
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
    # 아래코드는 비효율적. 선형적으로 나란히 연결되어있을경우 O(V)
    # if parent[x] != x:
    #     return find_parent(parent, parent[x]) 
    # return x
        

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split()) # 노드개수, 간선개수
parent = [[0] * (v+1)] # 부모 테이블 초기화

# 부모를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i
# Union 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합:', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()
# 부모 테이블 내용 출력하기
print('부모 테이블:',end='')
for i in range(1, v+1):
    print(parent[i],end=' ')
