'''
날짜: 2022.12.25
시간복잡도:

문제:
소문자로 변경하고, 사전 오름차순 정렬해라
풀이:
20:25~20:27(2분)

'''
def solution(my_string):
    li = my_string.lower()
    li = sorted(li)
    return ''.join(li)

def solution(my_string):
    li = list(my_string.lower())
    li = sorted(li)
    return ''.join(li)