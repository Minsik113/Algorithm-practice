'''
하나씩 dictionary에 넣으면 O(N)에 가능할 듯?
'''
def solution(n):
    answer = 0
    c = 0
    for i in range(1,n+1):
        c += 1
        while True:
            # 1. 3의 배수가 아니고, 숫자 3이 없으면 탈출
            if c % 3 != 0 and '3' not in str(c):
                break
            # 2.그 외라면 c 1증가
            c += 1
    return c