'''
날짜: 2022.09.29
시간복잡도:

문제: https://www.acmicpc.net/problem/11659
idx가 a~b인 애들의 합을 구해라

풀이방식:
19:30 ~ 

부분합을 저장해두는 dictionary를 만들자.
값이 있으면 쓰고, 없으면 생성

'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
number = list(map(int, input().split()))
temp = 0

# 부분합 저장
list_sum_arr = [0] # 0번째항 만들어두면 좋음
for i in number: # O(N)
    temp = temp + i
    list_sum_arr.append(temp)

# print(list_sum_arr)
for i in range(m):
    a, b = map(int, input().split())
    print(list_sum_arr[b] - list_sum_arr[a-1])
