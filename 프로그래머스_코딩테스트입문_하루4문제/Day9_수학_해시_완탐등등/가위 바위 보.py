'''
날짜: 2022.12.04
시간복잡도: O(len(rsp))

문제:
풀이:
21:42~21:44
이기는 숫자를 넣어두면됨.

'''
def solution(rsp):
    answer = ''
    rsp_dict = {
        '2':'0'
        ,'0':'5'
        ,'5':'2'
    }
    for i in rsp:
        answer += rsp_dict[i]
    return answer

def solution(rsp):
    rsp_dict = {
        '2':'0'
        ,'0':'5'
        ,'5':'2'
    }
    return ''.join(rsp_dict[i] for i in rsp)