'''
  1 ~ n  순서로 놓여있다.
(맨위 ~ 맨아래)

맨위버리고
맨위를 맨아래로넣음
길이가 1이되면 종료

'''
from collections import deque

n = int(input())
array = deque([i for i in range(1, n+1)])
# print(array)

while True:
    if len(array) == 1:
        print(array[0])
        break
    # 맨위버림
    array.popleft()
    # 그다음꺼 아래로
    array.append(array.popleft())
