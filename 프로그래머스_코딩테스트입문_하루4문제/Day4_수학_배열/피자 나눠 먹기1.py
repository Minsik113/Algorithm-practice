'''
날짜: 2022.11.29
시간복잡도:

문제:
풀이:
22:06~22:08
n을 7로 나눈 몫 a, 나머지가 0이면 -> a개의 피자필요
n을 7로 나눈 몫 a, 나머지가 b이면 -> a+1개의 피자필요
'''
def solution(n):
    a = n // 7 
    if n % 7 == 0:
        return a
    return a+1

def solution(n):
    return n//7 + (1 if n%7 else 0)