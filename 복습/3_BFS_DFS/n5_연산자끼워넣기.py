from itertools import permutations

n = int(input()) # 수의개수
numbers = list(map(str, input().split()))
oper_type = ['+', '-', '*', '/']
oper_count = list(map(int, input().split()))

# 사용할 수 있는 연산자 종류 체크
operators = dict()
for i in range(4):
    operators[oper_type[i]] = oper_count[i]

# operators로 n-1개의 모든경우 수 생성해라. 중복x = 순열
row = [''] *(n-1)
result = []
def solve(depth):
    if depth == n-1: # row에 연산자배열 
        save = numbers[0]
        for i in range(n-1):
            save = eval(str(save) + row[i] + numbers[i+1])
            save = int(save)
        result.append(save)
        return
    for i in range(4): # 연산자 1개씩 넣어준다
        row[depth] = oper_type[i]
        if check(depth):
            operators[row[depth]] -= 1
            solve(depth+1)
            operators[row[depth]] += 1
def check(depth):
    if operators[row[depth]] > 0:
        return True
    return False

solve(0)
print(result)


print(max(result))
print(min(result))

# solve(0)
