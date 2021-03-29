# 1/14
# 걸린시간: 14분
# pypy3로 제출해야 시간초과 안남.
data = list(input())
n = int(input())

l_stack = data[:] 
r_stack = []

for _ in range(n):
    one = list(input())
    if one[0] == 'P':
        l_stack.append(one[2])
    elif one[0] == 'L':
        if l_stack:
            r_stack.append(l_stack.pop())
    elif one[0] == 'D':
        if r_stack:
            l_stack.append(r_stack.pop())
    elif one[0] == 'B':
        if l_stack:
            l_stack.pop()
    else:
        print('error')
        exit()
l_stack.extend(reversed(r_stack))
print(''.join(l_stack))
