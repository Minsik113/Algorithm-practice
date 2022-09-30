'''
날짜: 2022.09.29
시간복잡도:

문제: https://www.acmicpc.net/problem/10986
풀이방식:
21:05 ~ 

1. 부분합 맵 만든다 
  1-1. 대각행렬은 입력받은 값으로 푼다 -> 메모리 초가
'''
n, m = map(int,input().split())
numbers = list(map(int, input().split()))
cnt = 0

# 1. 맵생성
arr = [0] * (n+1)
for i in range(1, n+1):
    arr[i] = arr[i-1] + numbers[i-1]
    
print(arr)


# 방법1 -> 메모리초과. 책 잘못나옴
# n, m = map(int,input().split())
# numbers = list(map(int, input().split()))
# cnt = 0

# # 1. 맵생성
# arr = [[0]*(n+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(i, n+1):
#         arr[i][j] = arr[i][j-1] + numbers[j-1]

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if arr[i][j] != 0 and arr[i][j] % m == 0:
#             cnt += 1

# print(cnt)            