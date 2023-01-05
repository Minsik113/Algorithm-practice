'''
날짜: 2022.12.25
시간복잡도:

문제:
4개의 점을 준다. 두 직선이 평행이면 1 리턴, 아니면 0

풀이:
22:43~22:46
방법1.기울기
1.하나잡고 3개의 선분과 연결해서 기울기 구해라
2.기울기 같ㅋ은게 나오면 1리턴하고 종료

'''
from itertools import permutations

def solution(dots):
    answer = 0
    for i in permutations([0,1,2,3],4):
        print(i)
    
    return answer