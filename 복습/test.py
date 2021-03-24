'''
'''
from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
oper = ['+', '-', '*', '/']
num = list(map(int, input().split()))

# 1. 가능한 연산자 조합
row = [''] * (n-1) # 백트래킹

# row[depth]에 oper[i]를 넣을 수 있어?
def check(idx):
    if num[idx] > 0:
        return True
    return False

min_value = int(1e9)
max_value = -int(1e9)

def solve(depth):
    global min_value, max_value
    # 다찼으면 계산시작
    if depth == n-1: 
        pre = numbers[0]
        for i in range(1, n):
            pre = int(eval(str(pre) + row[i-1] + str(numbers[i])))
        
        # 계산끝났으니 갱신해주고 종료
        min_value = min(min_value, pre)
        max_value = max(max_value, pre)
        return

    for i in range(4):
        if check(i):
            row[depth] = oper[i] # 넣어주고
            num[i] -= 1 # 값 하나줄임
            solve(depth+1)
            row[depth] = '' # 원상태로
            num[i] += 1 # 값 원상복구

solve(0)
print(max_value)
print(min_value)

# possible = []
# for i in permutations(op, n-1):
#     possible.append(list(i))

# # 2. 숫자계산
# min_value = int(1e9)
# max_value = -int(1e9)
# while possible:
#     op = possible.pop()
#     pre = numbers[0]
#     for i in range(1, n):
#         pre = int(eval(str(pre) + op[i-1] + str(numbers[i])))
#     min_value = min(min_value, pre)
#     max_value = max(max_value, pre)
# print(max_value)
# print(min_value)