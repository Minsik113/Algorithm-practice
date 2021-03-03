'''
100C11 은 수가 너무큼. Permutation못쓴다.
'''
T = int(input())
number = list(map(int, input().split()))
oper_num = list(map(int, input().split()))
oper_type = ['+','-','*','/']

# 전체 연산자: 종류 - 개수
operators = dict()
for i in range(4):
    operators[oper_type[i]] = oper_num[i]

def check(depth):
    if operators[row[depth]] > 0:
        return True
    return False
# 가능한 연산자를 뽑자.
max_value = 0
min_value = int(1e9)
def solve(depth):
    global max_value
    global min_value
    if depth == T-1: # 연산자 골라졌음. 계산하자
        prev = number[0]
        for i in range(T-1):
            prev = int(eval(str(prev) + row[i] + str(number[i+1])))
        max_value = max(max_value, prev)
        min_value = min(min_value, prev)
        return
        
    for i in range(4): # 연산자 하나씩 넣어본다
        row[depth] = oper_type[i] 
        if check(depth): # 가능하다면
            operators[row[depth]] -= 1
            solve(depth+1) # 다음꺼봄
            operators[row[depth]] += 1
row = [''] * (T-1)
solve(0)
print(max_value)
print(min_value)
