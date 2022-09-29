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
arr = list(map(int, input().split()))
result = [] 

# 부분합 저장
list_sum_arr = [0] * n 
list_sum_arr[0] = arr[0] # 1번째 항
for i in range(1, n): # O(N)
    list_sum_arr[i] = list_sum_arr[i-1] + arr[i]
print(list_sum_arr)
for i in range(m):
    a, b = map(int, input().split())
    print(list_sum_arr[b-1] - list_sum_arr[a-1])
