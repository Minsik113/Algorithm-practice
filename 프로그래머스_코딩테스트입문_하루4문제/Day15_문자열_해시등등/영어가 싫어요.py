'''
날짜: 2022.12.20
시간복잡도:

문제:
풀이:
16:33~16:38(5분)
방법1. 조건문
문자열을 다 잘라봐야한다. if문으로 가야겠네?
방법2. replace로 대체

'''
def solution(numbers):
    li = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for idx,eng in enumerate(li):
        numbers = numbers.replace(eng,str(idx))
    return int(numbers)

def solution(numbers):
    answer = ''
    idx = 0
    while idx < len(numbers):
        if numbers[idx] == 'z':
            answer += '0'
            idx += 4
        elif numbers[idx] == 'o':
            answer += '1'
            idx += 3
        elif numbers[idx] == 'e':
            answer += '8'
            idx += 5
        elif numbers[idx] == 'n':
            answer += '9'
            idx += 4
        elif numbers[idx] == 't':
            if numbers[idx+1] =='w':
                answer += '2'
                idx += 3
            else:
                answer += '3'
                idx += 5
        elif numbers[idx] == 'f':
            if numbers[idx+1] =='o':
                answer += '4'
                idx += 4
            else:
                answer += '5'
                idx += 4
        else: # numbers[idx] == 's':
            if numbers[idx+1] =='i':
                answer += '6'
                idx += 3
            else:
                answer += '7'
                idx += 5
    return int(answer)