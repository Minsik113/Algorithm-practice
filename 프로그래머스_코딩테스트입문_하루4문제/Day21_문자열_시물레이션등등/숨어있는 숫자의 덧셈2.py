'''
날짜: 2023.01.02
시간복잡도:

문제:
풀이:
10:38~22:43(5분)
자연수만 골라서 더해라
'''
def solution(my_string):
    s = ''.join(s if s.isdigit() else ' ' for s in my_string)
    return sum(int(i) for i in s.split())
    
def solution(my_string):
    answer = 0
    temp = ''
    for s in my_string:
        if s.isdigit():
            temp += s
        elif temp != '': # temp = 숫자
            answer += int(temp)
            temp = ''
        else: # temp = ''
            pass
    
    if temp != '':
        answer += int(temp)
        
    return answer