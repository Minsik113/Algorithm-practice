'''
1~N k

1. array에서 k번째수를 뺀다. 
2. 뺀곳부터 뒤에서k번째를 뺀다
3. 1,2번 반복해서 len(array) == 0 일떄까지 반복한다.
4. 뺀 순서를 출력해라

-> 맨위를 맨끝으로 넣으면서 원형태를 만든다
-> k번쨰 에서 pop하면됨
'''

from collections import deque

n, k = map(int, input().split())
array = deque([i for i in range(1, n+1)])
result = [] # 출력되는 순서 저장하는 리스트

index = 1
while len(array) != 0:
    if index == k:
        result.append(array.popleft())
        index = 1
    else:
        index += 1
        array.append(array.popleft())

# print(result)
print('<', end='')
for i in range(len(result)-1):
    print(result[i],end=', ')
print(result[-1],end='')
print('>')