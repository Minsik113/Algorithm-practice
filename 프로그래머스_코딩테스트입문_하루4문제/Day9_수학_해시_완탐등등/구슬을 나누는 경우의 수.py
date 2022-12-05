'''
날짜: 2022.12.05
시간복잡도: O(1)

문제:
풀이:
조합 수식이용
'''
def solution(balls, share):
    answer = 1
    for i in range(balls,balls-share,-1):
        answer = answer * i
        print(i,answer)
        
    temp = 1
    for i in range(1, share+1):
        temp = temp * i
    
    answer //= temp
    return answer