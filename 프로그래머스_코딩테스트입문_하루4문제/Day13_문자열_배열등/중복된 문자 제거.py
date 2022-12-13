'''
날짜: 2022.12.13
시간복잡도: O(len(my_string))

문제:
풀이:
set()를 써서 봐야 시간복잡도 빠를거같다
'''
def solution(my_string):
    answer = ''
    check_set = set()
    for i in my_string:
        if i not in check_set:
            check_set.add(i)
            answer+=i
    return answer