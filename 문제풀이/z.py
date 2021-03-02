from itertools import permutations

n =  int(input())
num = list(map(int, input().split()))
oper_num = list(map(int, input().split()))
oper_type = ['+','-','*','/']
operator = ''
for i in range(4):
    operator += oper_type[i]*oper_num[i]

# oper 나올 수 있는 종류
oper = []
for i in permutations(operator, n-1):
    oper.append(list(i))

# num사이에 opertype넣으면됨
result = ''
max_value = 0
min_value = int(1e9)
while oper:
    prev = num[0]
    q = oper.pop()
    for i in range(1, n):
        strings = ''
        strings += str(prev) + q[i-1] + str(num[i])
        prev = int(eval(strings))
    # print(prev)
    max_value = max(max_value, prev)
    min_value = min(min_value, prev)

print(max_value)
print(min_value)

