# 나올 수 있는 연산자만 출력해보자
n = int(input())
numset = list(map(str, input().split()))
data = ['+','-','*','/']
count_operators = list(map(int, input().split()))
operators = dict()

# operators = [연산자,개수]
for i in range(4): 
    operators[data[i]] = count_operators[i]

# 여기에 저장
row = [''] * (n-1)
result = []
def solve(depth):
    if depth == n-1: # row에 저장이 다 되어있다.
        # print(''.join(map(str,row)))
        save = numset[0]
        for i in range(n-1):
            save = eval(str(save) + row[i] + numset[i+1])
            save = int(save)
        result.append(save)
        return
    for i in range(4): # 연산자 1개씩 넣어줘
        row[depth] = data[i]
        if check(depth):
            operators[row[depth]] -= 1
            solve(depth+1)
            operators[row[depth]] += 1

# row[depth] = '+' 가 들어올 수 있는지 체크
# 연산자의 operators의 개수를
def check(depth):
    if operators[row[depth]] > 0 :
        return True
    return False

solve(0)
print(max(result))
print(min(result))