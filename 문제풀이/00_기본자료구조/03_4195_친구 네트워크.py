# 1/14
# 문제 유형: 해시, 집합, 그래프
# 추천 풀이 시간: 50분

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y: # 부모가 다르면 합쳐줘야지
        parent[y] = x
        number[x] += number[y]


def find(x):
    if x == parent[x]: 
        return x

    else: # 대표가 자기자신이 아니라면 = 이미 연결 되었다면
        p = find(parent[x])
        parent[x] = p
        return parent[x] # 대표인 애를 출력

import sys


x = int(sys.stdin.readline())
answer = []

for _ in range(x):
    parent = dict()
    number = dict()

    n = int(sys.stdin.readline())
    
    for _ in range(n):
        x, y = sys.stdin.readline().rstrip().split(' ')
        
        if x not in parent: # 새로 들어온 애라면
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union(x, y)
        answer.append(number[find(x)])

for i in answer:
    print(i)


# 나동빈

# 1/ 해시를 활용한 Union-Find 알고리즘을 이용해 문제를 풀 수있다.
# 2/ Python에서는 dictionary자료형을 해시처럼 사용할 수 있다
# union-find
#   원소들의 연결 여부를 확인하는 알고리즘
#   더 작은 원소를 부모로 삼도록 설정
#  값   1 2 3 4
#  부모 1 2 3 4  
# 1-4  2-4 라면)
#  값   1 2 3 4
#  부모 1 1 3 1  이 됨. 총 2개의 집합.
# 결과: {1,2,4}, {3}

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y: # parent[y] = x
        parent[y] = x
        number[x] += number[y]

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

import sys
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    parent = dict()
    number = dict()

    f = int(sys.stdin.readline())

    for _ in range(f):
        x, y = sys.stdin.readline().rstrip().split(' ')
        
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        union(x, y)
        print(number[find(x)])
