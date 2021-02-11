# 1/12 백준, 1874, 스택수열

n = int(input())

stack = [] # 스택 쌓을 리스트
answer = [] # 정답 넣을 리스트
count = 1

for i in range(1,n+1): # 1 ~ n+1
    x = int(input())
    
    while count <= x:
        stack.append(count)
        count += 1
        answer.append('+')

    # Top에 원하는 숫자가 있다면 pop
    if stack[-1] == x: 
        answer.append('-')
        stack.pop()
    
    # 원하는 숫자가 아니라면
    else:
        print('NO')
        exit(0)

print('\n'.join(answer))
        
# 동빈나

# 1. 원소 삽입할 때는, 특정 수에 도달할 때까지 삽입하면 된다.
# 2. Point 배열이 다 사용되었을때는 남은 것들은 
# 내림차순이어야 자연스럽게 쭉 뺼 수 있다.
n = int(input)

count = 1
stack = []
result = []

for i range(1, n+1): # 데이터 개수만큼 반복
    data = int(input())
    while count <= data: # 입력 받은 데이터에 도달할 때까지 삽입
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data: # 스택 최상위 원소가 데이터와 같을 때 출력
        stack.pop()
        result.append('-')
    else: # 불가능한 경우
        print('NO')
        exit(0)

print('\n'.join(result)) # 가능한 경우


