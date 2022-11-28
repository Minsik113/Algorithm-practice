'''
날짜: 2022.11.28
시간복잡도: O(N)

문제:
입력의 2배값 출력

풀이:
19:59 ~ 
값이 음수면 2곱하고 -붙여줌

'''
def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(number * 2)
    
    return answer

def solution(numbers):
    return [num*2 for num in numbers]