'''
날짜: 2022.11.29
시간복잡도:

문제:
풀이:
22:12~22:17
6과n의 최소공배수

'''
def GCD(a,b):
    while b>0:
        a,b = b,a%b
    return a
def LCD(a,b):
    return (a*b)//GCD(a,b)
    
def solution(n):
    answer = 0
    return LCD(6,n) // 6
