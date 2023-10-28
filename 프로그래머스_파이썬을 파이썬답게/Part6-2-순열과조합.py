####################
# 날짜: 2023.10.28
# 시간복잡도:
# 해결시간: 9분 (20:51~21:00)
# 포인트:
# itertools의 순열(permutations) 조합(combinations) 대해 아는가
#
#
####################

import itertools
def solution(mylist):
    answer =[list(i) for i in itertools.permutations(mylist)]
    sortAnswer = answer[:]
    sortAnswer.sort()
    print(answer)
    print(sortAnswer)
    return sortAnswer