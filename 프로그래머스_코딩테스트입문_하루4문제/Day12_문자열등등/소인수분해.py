'''
날짜: 2022.12.12
시간복잡도:

문제:
풀이:
소인수분해해라 -> 약수 set을 찾아라
나온 숫자를 소인수분해 한 dict이 필요하다. 이걸보면서 최소한으로 체크해야함.
'''
import math
def solution(n):
    answer = []
    real = dict() # 해당 숫
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            print(i, n//i)
        
    return answer
    
# def check(n):
#     cnt = 0 
#     res = []
#     for i in range(2,n):
#         if n % i == 0: # i로 나누어짐
#             res = [i, n//i]
#             cnt = 1
#             print(cnt,res)
#             break
#     if cnt == 1:
#         return res
#     else:
#         return [0,0]
    
# def solution(n):
#     answer = []
#     answer_set = set()
#     z = check(n)
#     # 1외에 약수 없으면 출력
#     if z[0] == 0:
#         return [n]
#     # 반복문으로 넣어야한다.
#     while True:
#         if z[0] == 0:
#             break
#         answer_set.add(z[0])
#         z = check(z[1])
#     print(answer_set)
#     return answer
