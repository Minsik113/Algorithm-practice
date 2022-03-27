'''
recursive function
하나의 함수에서 자기자신을 다시 호출하여 작업을 수행하는 것. 
많은 문제가 재귀로 풀리기도 한다.
Recursive version(재귀)-O(n) vs Iterative version(반복문)-O(n)
이진트리(binary trees)
'''

def solution(n):
    if n < 1:
        return 1
    else:
        return n*solution(n-1)
print(solution(5))

# 피보나치 순열 (Fibonacci 순열) - Recursive version
def solution(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return solution(x-1) + solution(x-2)
print(solution(10))

def solution(x):
    return x if x<2 else solution(x-1) + solution(x-2)
print(solution(10))

# 피보나치 순열 (Fibonacci 순열) - Iterative version
def solution(x):
    pre1 = 0  # Fn-1
    pre2 = 1  # Fn-2
    temp = 0  # Fn 
    cnt  = 1  # 현재 몇 번째인가
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        while True:
            cnt += 1
            temp = pre1 + pre2
            if cnt == x:
                break
            pre1 = pre2
            pre2 = temp
        return temp
print(solution(10))
