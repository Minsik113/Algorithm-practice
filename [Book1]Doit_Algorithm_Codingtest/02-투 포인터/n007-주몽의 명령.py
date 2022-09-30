'''
날짜: 2022.09.30
시간복잡도:

문제: https://www.acmicpc.net/problem/1940
풀이방식:
23:28 ~ 

'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input()) # m이 되면 result 증가
result = 0 
arr = list(map(int, input().split()))
arr.sort()

start_index = 0 # index 저장
end_index = n-1

while end_index<n and start_index <= end_index:
    temp = arr[start_index] + arr[end_index]
    # 1. 찾으면 앞에 당김
    if temp == m:
        result += 1
        start_index += 1
    # 2. 합이 크면, 앞 짧게
    elif temp > m:
        end_index -= 1
    # 3. 합이 작으면, 더길게 
    else:
        start_index += 1

print(result)