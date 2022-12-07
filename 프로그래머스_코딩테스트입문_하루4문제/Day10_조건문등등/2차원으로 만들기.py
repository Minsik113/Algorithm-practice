'''
날짜: 202.12.07
시간복잡도:

문제:
풀이:
num_list를 n개씩 묶으면됨
'''
def solution(num_list, n):
    answer = []
    s = 0
    b = n
    while True:
        if len(num_list)<b:
            break
        answer.append(num_list[s:b])
        s=b
        b+=n
    
    return answer