'''
날짜: 2022.12.25
시간복잡도:

문제:
원소에 n이 들어가 있는지만 보면 됨

풀이:
20:58~21:09(11분)

'''
def solution(array, n):
    return array.count(n)
    
def solution(array, n):
    return sum([1 for i in array if i==n])

def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer+=1
        
    return answer