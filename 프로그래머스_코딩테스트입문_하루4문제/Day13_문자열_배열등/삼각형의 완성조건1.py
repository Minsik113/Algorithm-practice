'''
날짜: 2022.12.13
시간복잡도:

문제:
풀이:
제일 긴 숫자뽑아서 나머지2개의 합보다 작은지 체크
'''
def solution(sides):
    s = sorted(sides,reverse=True)
    if sum(s) - 2*s[0] > 0:
        return 1
    return 2