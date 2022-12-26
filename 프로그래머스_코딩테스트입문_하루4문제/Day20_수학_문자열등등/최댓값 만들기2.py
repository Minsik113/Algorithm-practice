'''
마이너스 플러스 따로 분류해서 제일 큰애 2개의 합을 비교하자
'''

def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 

def solution(numbers):
    answer = 0
    number = sorted(numbers)
    
    front = 1
    cnt = 0
    while cnt != 2:
        front *= number[cnt]
        cnt += 1
    
    end = 1
    cnt = -1
    while cnt != -3:
        end *= number[cnt]
        cnt -= 1
    # print(front, end)
    
    return max(front,end)