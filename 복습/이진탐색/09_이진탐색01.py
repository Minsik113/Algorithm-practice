# 1/20
# 블로그
# https://cjh5414.github.io/binary-search/
# 백준
# https://www.acmicpc.net/problemset?sort=ac_desc&algo=12
# 양의 정수 N 이 주어졌을 때 N의 제곱근 √N 을 구하는 
# 소스코드를 작성해보자. 단, 제곱근 값이 정수 일 경우에만 출력한다.

################  ################
# O(N) - 자연수 크기만큼 봐야함
import math

n = int(input())

for i in range(n):
    if i*i == n:
        print(i)
        exit()
print(-1)

################  ################
# 0부터 N까지의 자연수 중에 N의 제곱근이 있는지 찾아보고 있다.
# 0 ~ N까지의 정렬된 자연수에서 특정 값을 찾고있는 것이다.
# 이진탐색 사용하면 O(logN)까지 줄일 수 있다.
# 양의 정수 N 이 주어졌을 때 N의 제곱근 √N 을 구하는 소스코드를 작성해보자.
# 단, 제곱근 값이 정수 일 경우에만 출력한다.

def bsearchTree(n):
    start = 0
    end = n

    while (start <= end):
        guess = (start + end) // 2
        if guess * guess == n:
            return guess
        elif guess*guess > n:
            end = guess - 1
        else:
            start = guess + 1

    return -1


n = int(input())
ans = bsearchTree(n)
print(ans)
