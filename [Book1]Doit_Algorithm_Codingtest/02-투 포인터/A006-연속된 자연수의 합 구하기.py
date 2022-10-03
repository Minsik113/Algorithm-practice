'''
날짜: 2022.10.04
시간복잡도: O(N)

문제: https://www.acmicpc.net/problem/2018
풀이방식:
01:40 ~ 01:55

n = 1000만임.  O(N)

연속된 숫자의 합을 찾는거니까 투포인터로 a~b 까지 합을 구한다.
O(N)에 끝낼수있음

1.부분합을 저장한 리스트를 만들어 둬도됨 -> 메모리초과
2.그때그때계산
'''
n = int(input())

# 1.반복문 시작
start_index = 1
end_index = 1
cnt = 1 # 자기자신
total = 1 # a ~ b 까지 합
while end_index < n:
    # 1-1. 연속 수 합이 목표값(n)과 같다면, cnt증가 / 다음 수 더함
    if total == n:
        cnt += 1
        end_index += 1
        total += end_index
    # 1-2. 연속 수 합이 목표값(n)보다 크면, start를 당겨야함.
    elif total > n:
        total -= start_index
        start_index += 1
    # 1-3. 연속 수 합이 목표값(n)보다 작다면, end를 더 민다
    else:
        end_index += 1
        total += end_index
print(cnt)
        






# ----------------------------
# 2022.10.04 메모리 초과 ^^;;
# ----------------------------
# n = int(input())
# # 1. 부분합 저장
# arr = [0] * (n+1)
# for i in range(1, n+1):
#     arr[i] = arr[i-1] + i
# # print(arr)
# # 2. 연속된 수의 합 찾기
# start_index = 0
# end_index = 1
# cnt = 0
# while end_index <= n:
#     # 2-1. 합이 더 작다 -> end늘려서 더 길게
#     if arr[end_index] - arr[start_index] < n:
#         end_index += 1
#     elif arr[end_index] - arr[start_index] > n:
#         start_index += 1
#     else:
#         end_index += 1
#         cnt += 1
#         # print(f'{start_index+1},부터,{end_index-1}')
# print(cnt)

