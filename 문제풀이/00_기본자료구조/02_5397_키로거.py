n = int(input())

for i in range(0,n):
    x = input()
    l_stack = []
    r_stack = []

    # 문자열 검색
    for k in range(0,len(x)):
        if x[k] == '<':
            if len(l_stack) != 0:
                r_stack.append(l_stack.pop())
            else:
                pass

        elif x[k] == '>': # r_stack이 l_stack으로 넘어오면됨
            if len(r_stack) != 0:
                l_stack.append(r_stack.pop())
            else: # 줄게 없으면 pass
                pass

        elif x[k] == '-': # 지울때는 현재위치에서지우니까 왼쪽지움
            l_stack.pop()
        
        else: # 문자, 숫자라면 현재커서의 왼쪽에 추가해주면됨.
            l_stack.append(x[k])

    # l_stack과 r_stack에 쭉 쌓이겠지. 출력해라
    l_stack.extend(reversed(r_stack))
    answer = "".join(l_stack)
    print(answer)


        
# 나동빈
# 현재 커서 위치를 계속 지정해 줘야할 것 같으니 힘들어보임
# 스택 자료구조 2개를 이용하면 간단함.
# 1. 문자열의 크기가 최대 1백만 이므로 시물레이션 방식으로는 문재 해결 x
# 2. 스택을 활용. 선형시간안에 문제를 해결할 알고리즘 설계. ex) O(n)

# [스택] [커서] [스택]
# 추가할땐 왼쪽스택에
# <는 왼쪽스택을 오른쪽스택으로보내줌
# >는 반대
# - 는 왼쪽스택에서 제거
# 23분 40초 이어보기


# 10^6인데 2중 for문하면 시간초과. 
# 스택 2개쓰자

n = int(input())

for _ in range(n):
    l_stack = []
    r_stack = []
    data = input()

    for k in data:
        if k == '<':
            if l_stack: # l_stack이 비어있지 않으면
                r_stack.append(l_stack.pop())
        elif k == '>':
            if r_stack:
                l_stack.append(r_stack.pop())
        elif k =='-':
            if l_stack:
                l_stack.pop()
        else: # 문자열이면 추가
            l_stack.append(k)
    
    l_stack.extend(reversed(r_stack))
    print(''.join(l_stack))



