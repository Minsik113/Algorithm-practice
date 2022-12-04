'''
날짜: 2022.12.04
시간복잡도:

문제:
풀이:
21:21~21:33

1. n을 1부터 소인수분해

'''
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += 1
            
    return answer

    
def solution(n):
    answer = 0
    arr = []
    # 1. n의 절반까지만 확인한다. 순서만 바꾸면 되는거라 x2하면 된다.
    for i in range(1,n+1):
        if n % i == 0:
            arr.append([i,n//i])
    # print(arr)
    # 2. [a,b]에서 a<b일때 index가 짝수인지 홀수인지 체크
    # for a,b in arr:
    #     if a<b:
    #         answer += 1
    #     else:
    #         if answer % 2 == 0:
    #             answer = answer*2
    #             answer += 1
    #         else:
    #             answer = answer*2
    #         break
            
    return len(arr)