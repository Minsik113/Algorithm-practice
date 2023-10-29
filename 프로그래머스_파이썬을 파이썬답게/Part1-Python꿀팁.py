####################
# 날짜: 2023.10.15
# 시간복잡도:
# 해결시간: 
# 포인트:
# for문을 써서 푸는건 파이썬스럽게 푸는게아니다. Java나 C처럼 해결하는것이다. 이번 공부를 통해 파이써닉하게 작성하는 공부를해보자.
#
#
####################



def solution(mylist):
    # answer = []
    # for i in mylist:
    #     answer.append(len(i))
    # return answer
    # return [len(i) for i in mylist]
    return list(map(len, mylist))