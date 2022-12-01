'''
날짜: 2022.12.01
시간복잡도:

문제:
풀이:
23:34~23:34
[짝수 개수,홀수 개수]
'''
def solution(num_list):
    answer = [0,0]
    for i in num_list:
        if i%2==0:
            answer[0]+=1
        else:
            answer[1]+=1
    return answer

# 이렇게 해도되네
def solution(num_list):
    answer = [0,0]
    for i in num_list:
        answer[i%2]+=1
        
    return answer