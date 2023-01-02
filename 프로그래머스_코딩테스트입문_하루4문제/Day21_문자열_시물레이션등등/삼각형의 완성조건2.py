'''
날짜: 2023.01.02
시간복잡도:

문제:
풀이:
20:07~20:16(9분)
방법1. 모든 경우 다 보기
다른 사람 풀이들은 왜 짧지?

'''
def solution(sides):
    return 2 * min(sides) - 1
    
def solution(sides):
    answer = 0
    s = []
    for i in sides:
        s.append(i)
        
    for i in range(1, sum(sides)+1):
        s.append(i)
        m = max(s)
        temp = 0
        check = False # 동일한 숫자가 나올 수도 있다.
        for j in range(3):
            if s[j] == m:
                if not check: # 
                    check = True
                else: # 이미 본 숫자라면
                    temp += s[j]
            else:
                temp += s[j]
        if m < temp:
            answer += 1
        s.pop()
    return answer