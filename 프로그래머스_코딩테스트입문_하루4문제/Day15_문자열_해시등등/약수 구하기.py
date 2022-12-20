'''
날짜: 2022.12.20
시간복잡도: O(NloglogN)

문제:
약수 구하기. 

풀이:
16:57~17:02(5분)
방법1. 에라토스테네스의 채

'''
def solution(n): # math호출안함.
    answer = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            answer.add(i)
            answer.add(n//i)
    return sorted(list(answer))

import math
def solution(n):
    answer = set()
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            answer.add(i)
            answer.add(n//i)
    return sorted(list(answer))