def solution(n):
    answer = 0
    for i in range(n+1):
        if i%2==0:
            answer += i
    return answer

def solution(n):
    answer = 0
    for i in range(2,n+1,2):
        answer += i
    return answer

def solution(n):
    return sum([i for i in range(2, n+1, 2)])
    
