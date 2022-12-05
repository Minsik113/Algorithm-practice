'''
그리디.
공격력 높은애부터써라
5 3 1
'''
def solution(hp):
    answer = 0
    answer += hp // 5
    hp = hp % 5
    answer += hp // 3
    hp = hp % 3
    answer += hp 
    return answer