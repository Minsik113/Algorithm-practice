####################
# 날짜: 2023.10.27
# 시간복잡도:
# 해결시간: 5분
# 포인트:
# 너무쉬움
#
#
####################
# 1. 노가다방법
def solution(mylist):
    answer = []
    for i in mylist:
        answer.append(int(i))
    return answer

# 2. map함수 사용
def solution(mylist):
    return list(map(int, mylist))