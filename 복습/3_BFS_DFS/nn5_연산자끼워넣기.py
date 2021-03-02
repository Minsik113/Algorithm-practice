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
##########################################
##########################################
# 시간초과...
# from itertools import permutations

# n =  int(input())
# num = list(map(int, input().split()))
# oper_num = list(map(int, input().split()))
# oper_type = ['+','-','*','/']
# operator = ''
# for i in range(4):
#     operator += oper_type[i]*oper_num[i]

# # oper 나올 수 있는 종류
# oper = []
# for i in permutations(operator, n-1):
#     oper.append(list(i))

# # num사이에 opertype넣으면됨
# result = ''
# max_value = 0
# min_value = int(1e9)
# while oper:
#     prev = num[0]
#     q = oper.pop()
#     for i in range(1, n):
#         strings = ''
#         strings += str(prev) + q[i-1] + str(num[i])
#         prev = int(eval(strings))
#     # print(prev)
#     max_value = max(max_value, prev)
#     min_value = min(min_value, prev)

# print(max_value)
# print(min_value)

