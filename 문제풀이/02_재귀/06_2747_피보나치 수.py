# 1/18
# 문제 난이도: Bronze 3
# 문제 유형: 재귀함수
# 추천 풀이 시간: 15분

# 피보나치 수열: 재귀적 구현의 한계
# 트리모양인데, 약간만 수가 커지게 되면 같은수도 너무 많이 계산해야함.
# 이러한 것을 해결하기 위하여 DP(dynamic programming)를 배운다.



# 나동빈 

# 성공코드
# 단순 반복문으로 해야한다
n = int(input())
a, b = 0, 1
while n > 0:
    a, b = b, a+b
    n -= 1
print(a)


# 실패코드
# O(2^n) n=30이면 10억정도의 연산.
# 10^9니까 매우많은양의연산

import sys

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        p = fibo(n-1) + fibo(n-2)
        return p


data = [0,1]

x = int(sys.stdin.readline())

print(fibo(x))
