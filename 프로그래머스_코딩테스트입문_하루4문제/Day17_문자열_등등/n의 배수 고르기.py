'''
날짜: 2022.12.23
시간복잡도: O(N)

문제:
풀이:
22:04~22:06(2분)
모든 수가 n으로 나누어지는지 다 봐야한다. O(N)
'''
def solution(n, numlist):
    return [num for num in numlist if num%n==0]
    
def solution(n, numlist):
    answer = []
    for num in numlist:
        if num % n == 0:
            answer.append(num)
    return answer