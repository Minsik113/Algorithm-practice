'''
날짜: 2022.12.01
시간복잡도:

문제:
풀이:
23:35~23:35
단순하게 n번 곱해주면됨
'''
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer+=i*n
    return answer