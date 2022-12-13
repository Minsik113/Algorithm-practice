'''
날짜: 2022.12.13
시간복잡도:

문제:
풀이:
stack사용하면될듯

'''
def solution(s):
    answer = []
    for i in list(s.split(' ')):
        if i != 'Z':
            answer.append(int(i))
        else:
            answer.pop()
    return sum(answer)