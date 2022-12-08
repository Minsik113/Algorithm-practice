'''
날짜: 2022.12.07
시간복잡도:

문제:
풀이:
한 번 봤던거를 또 보게하면 안된다. -> 메모라이즈 사용
'''
def solution(n):
    answer = 0
    m = [0] * 11 # 1~10팩토리얼까지 저장
    m[1] = 1
    m[2] = 2
    
    for i in range(1,11):
        if m[i] == 0:
            m[i] = m[i-1] *i
            
        if n <= m[i]:
            if n == m[i]:
                answer=i
            else:
                answer=i-1
            break
    return answer

def solution(n):
    answer = 1
    total = 1 # 다 곱한거
    while total <= n:
        answer += 1
        total *= answer
    answer -= 1
    return answer