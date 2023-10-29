####################
# 날짜: 2023.10.27
# 시간복잡도:
# 해결시간: 2분
# 포인트:
# 금방풀음
#
#
####################
# 1. 처음풀이
def solution(mylist):
    answer = []
    idx = 0
    for i in range(1, len(mylist)):
        answer.append(abs(mylist[idx] - mylist[i]))
        idx += 1
    return answer

# 2. idx가 필요없음
def solution(mylist):
    answer = []
    for i in range(len(mylist)-1):
        answer.append(abs(mylist[i+1] - mylist[i]))
    return answer

# 3. zip활용
def solution(mylist):
    answer = []
    for a,b in zip(mylist,mylist[1:]):
        answer.append(abs(a-b))
    return answer