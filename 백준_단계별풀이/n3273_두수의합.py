import sys
input = sys.stdin.readline
if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    data = sorted(data)
    x = int(input())
    # print(data)

    # 탐색 시작
    result = 0
    left = 0
    right = n - 1
    while left < right:
        temp = data[left] + data[right]
        if temp > x:
            right -= 1
        elif temp < x:
            left += 1
        else:
            # 조건만족
            result += 1
            # print('답:',data[left],data[right])
            left += 1
    print(result)

# import sys
# input = sys.stdin.readline

# n = int(input())
# data = list(map(int, input().split()))
# data = sorted(data)
# x = int(input())
# # print(data)

# # 탐색 시작
# result = 0
# left = 0
# right = n - 1
# while left < right:
#     temp = data[left] + data[right]
#     if temp > x:
#         right -= 1
#     elif temp < x:
#         left += 1
#     else:
#         # 조건만족
#         result += 1
#         # print('답:',data[left],data[right])
#         left += 1
        
# print(result)

