'''
7p1 + 7p2 .. + 7p7 로 모든 경우의수 확인가능
-> 순열사용 
모든 경우의수를 set()에 넣어 중복제거
각 수가 소수인지 체크 O(log(k)) 충분할듯?
'''
from itertools import permutations
import math
def solution(numbers):
    answer = 0
    data = list(map(str, numbers))
    length = len(numbers)
    
    save = dict()
    # 1개짜리
    for i in numbers:
        if i not in save:
            save[i] = 0
    # 2개짜리
    for i in range(2, length+1):
        for j in permutations(data,i):
            if j not in save:
                save[j] = 0
    # 계산시작
    check = dict()
    for num in save.keys():
        s = "".join(num)
        # 0,1은 소수가아님
        if int(s) <= 1: 
            continue
        if str(int(s)) not in check:
            check[s] = 1 # 봤다고 체크해두고
            flag = True
            # 소수 여부 확인
            for i in range(2, int(math.sqrt(int(s))+1)):
                if int(s) % i == 0:
                    flag = False # 소수라면 False
            if flag:
                answer += 1
                
    return answer

