'''
날짜: 2022.12.20
시간복잡도: O(N)

문제:
풀이:
16:10~16:12(2분)
code의 배수에 위치한 애들만 출력.
'''

def solution(cipher, code):
    return cipher[code-1::code]

def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher),code):
        answer += cipher[i]
    return answer