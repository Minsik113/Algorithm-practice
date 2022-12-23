'''
날짜: 2022.12.23
시간복잡도:

문제:
풀이:
22:03~22:04(1분)

'''
def solution(num, k):
    return str(num).find(str(k))+1 if str(num).find(str(k)) != -1 else -1

def solution(num, k):
    a = str(num).find(str(k))
    if a == -1:
        return -1
    else:
        return a+1