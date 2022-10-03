'''
날짜: 2022.10.04
시간복잡도: O(NlogN)

문제: https://www.acmicpc.net/problem/1940
풀이방식:
02:11 ~ 

두 수의 합으로 목표값을 만들면 되는거니까 정렬해서 투포인터 하면 O(NlogN)됨

'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))
cnt = 0 # 정답 저장
# 1.정렬
arr = sorted(arr)
# 2.투포인터
start_idx = 0
end_idx = n-1 # n개가 0 ~ n-1번으로 표현되어있으니
while start_idx < end_idx:
    # 2-1. 목표값보다 작으면, start늘림
    if arr[start_idx] + arr[end_idx] < m:
        start_idx += 1
    # 2-2. 목표값보다 크면, end줄임
    elif arr[start_idx] + arr[end_idx] > m:
        end_idx -= 1
    # 2-3. 목표값보다 같으면, cnt증가. end줄임
    else:
        cnt += 1
        end_idx -= 1
print(cnt)