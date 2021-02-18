n = int(input())
number = list(map(str, input().split()))
oper_num = list(map(int, input().split()))
operator_type = ['+','-','*','/']
operators = ""
oper_count = dict()

for i in range(4):
    operators += operator_type[i] * oper_num[i]
    oper_count[operator_type[i]] = oper_num[i]

length = len(operators)

row = [''] * (length)
result = []

def check(depth):
    if oper_count[row[depth]] > 0:
        oper_count[row[depth]] -= 1
        return True
    return False

def solve(depth):
    if depth == length: # 연산자 depth만큼 출력
        result.append(''.join(row))
        return
    for i in range(length):
        row[depth] = operators[i]
        if check(depth):
            solve(depth+1)
            oper_count[row[depth]] += 1
            row[depth] = ''
# 계산하는 함수     
answer = []
def calculate(result, number):
    for oo in result:
        s = number[0]

        for i in range(1, n):
            s += oo[i-1] + number[i]
            s = str(int(eval(s)))
        answer.append(int(s))

solve(0)
# print(number)
# print(result)
calculate(result, number)
print(max(answer))
print(min(answer))

