'''
날짜: 2022.12.23
시간복잡도:

문제:
풀이:
22:07~22:07(0분?)
방법1.
str로 바꿔서 각자리수 합을 구해라
방법2. 훨씬빠르다
일의자리부터 계산

'''
def solution(n):
    answer = 0
    while n:
        n,r = divmod(n, 10) # 몫 나머지
        answer += r
    return answer