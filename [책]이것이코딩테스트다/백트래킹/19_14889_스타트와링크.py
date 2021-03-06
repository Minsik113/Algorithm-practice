##########################################
##########################################
# 3/21 pypy3로는 됨
'''
같거나 작으면안된다
큰애들이랑만 짝가능하다.
두 팀으로 나눠서 팀끼리의 합을 구해라.
총합의 차중 가장 작은값은?
'''

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

row = []

# x를 넣어도되는지 본다. 오름차순이어야함
def check(x):
    # 먼저 들어가있는것들이 크거나 같으면 안됨.
    for j in range(len(row)): 
        if row[j] >= x:
            return False
    return True

# 팀을 구하자
min_value = int(1e9)
def solve():
    global min_value
    # 팀완성되었으면 합을 구하자
    if len(row) == n//2:
        one = 0
        theother = 0
        for a in range(n):
            for b in range(a+1, n):
                if a == b:
                    continue
                if a in row and b in row:
                    one += array[a][b] + array[b][a]
                elif a not in row and b not in row:
                    theother += array[a][b] + array[b][a]
        min_value = min(min_value, abs(one-theother))
    # 팀 완성안되었으면 넣으면됨
    for i in range(n):
        if check(i): # i를 넣어도 될까?
            row.append(i)
            solve() # 다음위치에 넣을꺼 찾아보자
            row.pop() #다시초기화

solve()
print(min_value)

##########################################
##########################################
# 3/21 combination풀이
from itertools import combinations

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
array = [i for i in range(n)]
min_value = int(1e9)
total = set()

for left in combinations(array, n//2):
    right = set()
    right = []
    for i in range(n):
        if i not in left:
            right.append(i)
    # 봤던거 안보기 위해서
    if left in total:
        break
    total.add(left)
    total.add(tuple(right))
    
    left = list(left)
    right = list(right)
    # left, right 합구하자
    l_sum, r_sum = 0, 0
    for i in range(len(left)):
        for j in range(len(right)):
            l_sum += data[left[i]][left[j]]
            r_sum += data[right[i]][right[j]]
    # print(left, right, l_sum, r_sum)
    min_value = min(min_value, abs(l_sum - r_sum))
print(min_value)
