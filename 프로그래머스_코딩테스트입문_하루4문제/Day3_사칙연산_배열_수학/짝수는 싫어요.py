'''
n보다 작은 홀수라면 answer에 넣는다.
answer를 오름차순 sorted한다.
'''
def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 == 1:
            answer.append(i)
    return sorted(answer)

def solution(n):
    return [i for i in range(1, n+1, 2)]