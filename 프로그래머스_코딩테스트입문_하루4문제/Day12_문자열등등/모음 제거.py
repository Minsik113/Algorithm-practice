def solution(my_string):
    answer = ''
    check = set()
    check.add('a')
    check.add('e')
    check.add('i')
    check.add('o')
    check.add('u')
    
    for i in my_string:
        if i in check:
            continue
        answer+=i
    
    return answer