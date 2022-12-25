'''
날짜: 2022.12.25
시간복잡도:

문제:
str1안에 str2가 있는지 체크

풀이:
20:29~20:30(1분)

'''
def solution(str1, str2):
    answer = 2
    if str2 in str1:
        answer=1
    return answer