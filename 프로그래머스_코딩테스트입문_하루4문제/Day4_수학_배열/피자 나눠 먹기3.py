'''
날짜: 2022.11.29
시간복잡도:

문제:
피자를 2~10조각으로 자를 수 있다.
n명의 사람이 최소 1조각 이상의 피자를 ㅓㅁㄱ으려면 최소 몇판의피자를 시켜야하는가

풀이:
22:17~
slice*N > n 이 되는 N값을 구하면됨

'''
def solution(slice, n):
    if n%slice == 0:
        return n//slice
    else:
        return n//slice + 1
        
def solution(slice, n):
    return n//slice+1 if n%slice else n//slice