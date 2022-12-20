'''
날짜: 2022.12.20
시간복잡도:

문제:
풀이:
16:14~16:19(5분)
단순변환 O(N)
 대문자 -> 소문자, 소문자 -> 대문자 
'''

def solution(my_string):
    answer = ''
    temp = ord('a')-ord('A')
    # print(ord('a'),ord('z'),ord('A'),ord('Z'))
    for i in my_string:
        # 소문자라면, 대문자로
        if 97 <= ord(i) and ord(i) <= 122: 
            answer += chr(ord(i)-temp)
        # 대문자라면, 소문자로
        else:
            answer += chr(ord(i)+temp)
    return answer