from itertools import permutations

n = int(input())
num = list(map(int, input().split()))

oper_type = ['+','-','*','/']
oper_num = list(map(int, input().split()))

operator = ''
for i in range(4):
    operator += oper_type[i] * oper_num[i]

def check(k):
    if oper_num[k] > 0:
        return True
    return False

def dfs(row, depth):
    if depth == n-1:
        print(row)
        return

    for i in range(4):
        if check(i):
            row[depth] = oper_type[i] # 넣고
            oper_num[i] -= 1 # 값하나줄여준다.
            dfs(row, depth+1) # 다음위치에 넣어본다
            oper_num[i] += 1
            row[depth] = ''
    
# 연산자가 들어갈 수 있는지 없는지만 계속 체크하면된다.
row = [''] * (n-1)
dfs(row, 0)





