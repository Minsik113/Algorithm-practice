'''
앞부터 하나씩 보는게 제일 빠를 듯? -> O(N)
'''
def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i!=letter:
            answer += i
    return answer

# 이게 더 멋진듯.
def solution(my_string, letter):
    return my_string.replace(letter,'')
