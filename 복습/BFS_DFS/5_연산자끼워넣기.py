from itertools import permutations

n = int(input()) # 수의개수
numbers = list(map(int, input().split()))
oper_type = ['+', '-', '*', '//']
oper_count = list(map(int, input().split()))

# 사용할 수 있는 연산자 종류 체크
operators = []
for i in range(4):
    for _ in range(oper_count[i]):
        operators.append(oper_type[i])

# operators로 n-1개의 모든경우 수 생성해라. 중복x = 순열
# print(operators)
result = []
max_value = 0
min_value = 1e9
for oper in permutations(operators,n-1):
    # oper의i와 numbers의i연결
    strings = str(numbers[0])
    for i in range(1,n):
        # print(strings)
        strings += oper[i-1] + str(numbers[i])
        strings = str(eval(strings))
    # string값이 나옴 이걸 result에 저장
    max_value = max(max_value, int(strings))
    min_value = min(min_value, int(strings))
    
print(max_value)
print(min_value)

# solve(0)
