'''
날짜: 2022.12.09
시간복잡도:

문제:
풀이:
'''
def solution(box, n):
    answer = 1
    for i in box:
        answer = (i // n) * answer
        
    return answer