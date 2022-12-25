'''
날짜: 2022.12.25
시간복잡도:

문제:
my_str을 길이 n씩 잘라서 저장. return은 list형식

풀이:
20:46~20:47(1분)
1.길이n으로 잘라서 answer에 append하기
'''
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0,len(my_str),n)]

def solution(my_str, n):
    answer = []
    for i in range(0,len(my_str),n):
        answer.append(my_str[i:i+n])
    return answer