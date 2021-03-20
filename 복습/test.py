'''
n개 수
n-1개 연산자
계산해라.

'''
# 수 입력 받는다
n = int(input())
numbers = list(map(int, input().split())) # 숫자배열

# 연산자 입력받는다
operators = ['+','-','*','/'] # 종류
operators_num = list(map(int, input().split())) # 종류마다 개수
oper_dict = dict() # 종류마다 몇 개 들어있는지
oper_total = "" # 한 줄로 합친다.
for i in range(4):
    oper_dict[operators[i]] = operators_num[i]
    if operators_num[i] != 0:
        oper_total += operators[i] * operators_num[i]

def check(depth):
    if oper_dict[row[depth]] > 0:
        oper_dict[row[depth]] -= 1
        return True
    return False

def calculate(row, depth):
    global min_value, max_value
    print(row,depth)
    # 가능한 연산자 찾았으니 계산한다
    if depth == n-1:
        # print(row)
        # pre = numbers[0]
        # for i in range(1, n): # 수 index, 연산자 index
        #     pre = int(eval(str(pre) + row[i-1] + str(numbers[i])))
        # max_value = max(max_value, pre)
        # min_value = min(min_value, pre)
        return
    # 4종류중 아무거나 넣는다.
    for i in range(4):
        row[depth] = operators[i]
        # 들어갈 수 있으면 -> depth증가해서 다음꺼넣어줌 
        if check(depth): 
            calculate(row, depth+1)
        row[depth] = '' # 들어갈 수 없다 or 함수끝남 -> 비워줌.
        print('q,',row,depth)


# 모든 경우 찾기 시작
max_value = 0
min_value = int(1e9)
row = [''] * (n-1)    
calculate(row, 0)

# print(max_value)
# print(min_value)