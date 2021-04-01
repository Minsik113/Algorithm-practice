##########################################
##########################################
# 4/1 훨씬 빠른 풀이 - 메모리 낭비도없고, 속도도 빠름.
import sys
input = sys.stdin.readline

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: 
        parent[b] = a # 작은쪽을 대표로 만듦
        count[a] += count[b] # 작은쪽에 그룹원 수 더함.
        return a
    elif a > b:
        parent[a] = b
        count[b] += count[a]
        return b
    else:
        return a
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    parent = dict() # 이름-이름
    count = dict()

    for _ in range(n):
        x, y = input().split()

        if x not in parent:
            parent[x] = x # x의 대표값 = x
            count[x] = 1 # 숫자
        if y not in parent:
            parent[y] = y
            count[y] = 1
        small = union_parent(parent, x, y)
        print(count[small])
##########################################
##########################################
# 4/1 - 첫 풀이. 비효율적인듯
# '''
# union-find써서 같은 그룹인지 체크해야함

# '''
# import sys
# input = sys.stdin.readline

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#         return (a, b)
#     else:
#         parent[a] = b
#         return (b, a)

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# test_case = int(input())
# for _ in range(test_case):
#     n = int(input())
#     min_value = 0
#     tree = dict() # 이름-고유번호?
#     parent = [0] * 200001 # 이름(숫자화) - 대표값
#     for i in range(1, 200001):
#         parent[i] = i

#     number = [1] * 200001 # 네트워크번호 - 친구들 수
#     serial_number = 1 # 고유번호
#     for i in range(n):
#         string1, string2 = input().split()
#         # 1. 이름마다 고유번호를 준다
#         if string1 not in tree:
#             tree[string1] = serial_number
#             serial_number += 1
#         if string2 not in tree:
#             tree[string2] = serial_number
#             serial_number += 1
        
#         # 2. 친구관계가 아니라면 -> 더 먼저들어온 애를 대표로하여 친구, 먼저들어온애의 그룹원 수 증가
#         if find_parent(parent, tree[string1]) != find_parent(parent, tree[string2]):
#             small, large = union_parent(parent, tree[string1], tree[string2])
#             # 대표값이 작은쪽에 수 추가하기
#             number[small] += number[large]
#             print(number[small])
#         # 3. 이미 친구관계인 애들이 들어오면 -> 더 큰애 출력
#         else: 
#             small, large = union_parent(parent, tree[string1], tree[string2])
#             print(number[small])

    