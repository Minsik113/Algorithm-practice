'''
날짜: 2023.01.03 -> 2023.01.18풀음
시간복잡도: O(1)

문제:
분수 -> 소수로 변경할 때, 유한소수인지 무한소수인지 파악하자.
분모의 소인수가 2와 5만 존재해야함.

풀이:
23:43~
기약분수로 나타냈을 때, 분모의 소인수가 2와 5만 존재해야한다.

1. a와 b의 최대공약수 구하기
2. 분모분자에 최대공약수를 나눈다. -> 기약분수
3. 분모가 2와5의 곱으로 표현이 되는지 파악.
'''

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def solution(a, b):
    temp = gcd(a, b)
    bb = b // temp
    
    while bb%5==0:
        bb = bb // 5
            
    while bb%2==0:
        bb = bb // 2

    if bb == 1:
        return 1
    else:
        return 2

from math import gcd
def solution(a, b):
    bb = b // gcd(a, b)
    
    while bb%5==0:
        bb = bb // 5
            
    while bb%2==0:
        bb = bb // 2
        
    return 1 if bb == 1 else 2
