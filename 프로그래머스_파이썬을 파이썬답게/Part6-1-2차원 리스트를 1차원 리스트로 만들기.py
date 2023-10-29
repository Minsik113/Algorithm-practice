####################
# 날짜: 2023.10.28
# 시간복잡도: O(N)
# 해결시간: 7분 (19:43~19:50)
# 포인트:
# 
#
#
####################
# 문제: 2차원 리스트를 1차원으로 만들기

# 1. 이중for문으로 만들기 O(N^2)
def solution(mylist):
    return [j for i in mylist for j in i]

# 2. +연산자로도 합칠 수 있다. O(N)
def solution(mylist):
    answer = []
    for i in mylist:
        answer += i
    return answer

# 3. sum 함수를 통해 빈리스트에 더한다
def solution(mylist):
    return sum(mylist, [])
