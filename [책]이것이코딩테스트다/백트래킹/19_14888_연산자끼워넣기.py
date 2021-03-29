##########################################
##########################################
# 3/20 복습
'''
n개의 숫자
n-1개의 연산자

'''
n = int(input())
number = list(map(int, input().split()))

# 가능한 연산자
oper_type = ['+','-','*','/']
operator_each_num = list(map(int, input().split()))
count_oper = dict() # 연산자들의 개수를 저장해놓은 dict()
for i in range(4):
    count_oper[oper_type[i]] = operator_each_num[i]
    
# operator에는 한줄로 세워둠. 
# count_oper에는 현재 남은 연산자들의 개수를 저장한 dict()

# 가능한 연산자 종류를 찾아볼까?
row = [''] * (n-1) 
max_value = int(-1e9)
min_value = int(1e9)
# x연산자를 depth위치에 넣어도 되는가?
def check(x, depth):
    if count_oper[x] > 0:
        return True
    return False

def solve(depth):
    global max_value, min_value
    # 원하는 개수 되었으니 계산
    if depth == n-1:
        pre = str(number[0])
        for i in range(1, n):
            pre = int(eval(str(pre) + row[i-1] + str(number[i])))
        max_value = max(max_value, pre)
        min_value = min(min_value, pre)
        return
    for i in range(len(oper_type)):
        # 연산자를 depth위치에 넣어도 되는가?
        if check(oper_type[i], depth):
            row[depth] = oper_type[i] # 넣고
            count_oper[row[depth]] -= 1
            solve(depth + 1) #다음depth를 본다
            count_oper[row[depth]] += 1
            row[depth] = '' # 다 사용했으니 원상복구

solve(0)
print(max_value)
print(min_value)
##########################################
##########################################
#
# # 나올 수 있는 연산자만 출력해보자
# n = int(input())
# numset = list(map(str, input().split()))
# data = ['+','-','*','/']
# count_operators = list(map(int, input().split()))
# operators = dict()

# # operators = [연산자,개수]
# for i in range(4): 
#     operators[data[i]] = count_operators[i]

# # 여기에 저장
# row = [''] * (n-1)
# result = []
# def solve(depth):
#     if depth == n-1: # row에 저장이 다 되어있다.
#         # print(''.join(map(str,row)))
#         save = numset[0]
#         for i in range(n-1):
#             save = eval(str(save) + row[i] + numset[i+1])
#             save = int(save)
#         result.append(save)
#         return
#     for i in range(4): # 연산자 1개씩 넣어줘
#         row[depth] = data[i]
#         if check(depth):
#             operators[row[depth]] -= 1
#             solve(depth+1)
#             operators[row[depth]] += 1

# # row[depth] = '+' 가 들어올 수 있는지 체크
# # 연산자의 operators의 개수를
# def check(depth):
#     if operators[row[depth]] > 0 :
#         return True
#     return False

# solve(0)
# print(max(result))
# print(min(result))