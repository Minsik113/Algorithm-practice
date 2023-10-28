####################
# 날짜: 2023.10.28
# 시간복잡도:
# 해결시간: 
# 포인트: map으로 리스트 각값에 함수를 적용하게 한다
# 
#
#
####################
def solution(mylist):
    answer = list(map(len, mylist))
    return answer

print(solution([[1],[2,3]]))