'''
날짜: 2022.12.12
시간복잡도:

문제:
풀이:
소인수분해해라 -> 약수 set을 찾아라
모든약수에서 소수인것만 찾으면된다?

'''
import math
def prime_number(num): # True -> 소수, False -> 소수x
    flag = True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            flag = False
            break
    if flag: return True
    else: return False
    
def solution(n):
    answer = set()
    end = int(math.sqrt(n))+1
    
    for i in range(2, end):
        if n % i == 0:
            print(i,n//i)
            # i가 소수인지 검사
            if (i not in answer) and prime_number(i):
                answer.add(i)
            # n//i가 소수인지 검사
            if (n//i not in answer) and prime_number(n//i):
                answer.add(n//i)
    
    if n not in answer and prime_number(n):
        answer.add(n)
        
    # 겹치는게 있을 수도 있다.
    return list(sorted(answer))

###
# 아래처럼 풀면 훨씬 오래걸린다.
###
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
                
    return answer