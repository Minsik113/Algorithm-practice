'''
날짜: 2022.12.20
시간복잡도:

문제:
풀이:
16:05~16:08(3분)
숫자의 자리수에 3,6,9가 들어간 개수만큼 return해라
'''
def solution(order):
    answer = 0
    for i in str(order):
        if i in ('3','6','9'):
            answer += 1
    return answer
