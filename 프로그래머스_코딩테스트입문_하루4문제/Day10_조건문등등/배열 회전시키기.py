'''
날짜: 2022.12.05
시간복잡도:

문제:
풀이:
right -> pop()해서 append()
left -> appendleft()해서 push()
deque이용
'''
from collections import deque
def solution(numbers, direction):
    answer = []
    q = deque(numbers)
    
    if direction =='right':
        q.appendleft(q.pop())
    else:
        q.append(q.popleft())
    answer=list(q)
    return answer

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction =='right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

def solution(numbers, direction):
    numbers = deque(numbers)
    numbers.rotate(1 if direction=='right' else -1)
    return list(numbers)