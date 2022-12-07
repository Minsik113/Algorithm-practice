def solution(dot):
    answer = 0
    x,y = dot
    # 1사분면
    if x>0 and x*y>0:
        answer=1
    elif x<0 and x*y>0:
        answer=3
    elif x<0:
        answer=2
    else:
        answer=4
    return answer

def solution(dot):
    answer = 0
    x,y = dot
    # 1,4
    if x*y > 0:
        return 1 if x>0 else 3
    else:
        return 4 if x>0 else 2