####################
# 날짜: 2023.10.26
# 시간복잡도: 
# 해결시간: 10분
# 포인트:
# zip()사용
#
#
####################
def solution(mylist):
    answer = []
    for i in zip(*mylist):
        answer.append(i)  
    return answer
