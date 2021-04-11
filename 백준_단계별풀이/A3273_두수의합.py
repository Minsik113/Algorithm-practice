# 4/11 - 성공
'''
n = 10^5
O(nlogn) = 약 700만

1. 정렬
2. 투포인터이용해서 target값과 비교하자.
if a[i]+a[j] < target:
    i++
elif a[i] + a[j] > target:
    j -=1
else:
    i += 1
    j -= 1 같은수가 없다는 조건이 있으니 이렇게함
'''
n = int(input())
array = list(map(int, input().split()))
target = int(input())

array.sort()
result = 0
i, j = 0, len(array) - 1
while i < j:
    if array[i] + array[j] < target:
        i += 1
    elif array[i] + array[j] > target:
        j -= 1
    else:
        result += 1
        i += 1
        j -= 1
print(result)

# import sys
# input = sys.stdin.readline
# if __name__ == '__main__':
#     n = int(input())
#     data = list(map(int, input().split()))
#     data = sorted(data)
#     x = int(input())
#     # print(data)

#     # 탐색 시작
#     result = 0
#     left = 0
#     right = n - 1
#     while left < right:
#         temp = data[left] + data[right]
#         if temp > x:
#             right -= 1
#         elif temp < x:
#             left += 1
#         else:
#             # 조건만족
#             result += 1
#             # print('답:',data[left],data[right])
#             left += 1
#     print(result)

# # import sys
# # input = sys.stdin.readline

# # n = int(input())
# # data = list(map(int, input().split()))
# # data = sorted(data)
# # x = int(input())
# # # print(data)

# # # 탐색 시작
# # result = 0
# # left = 0
# # right = n - 1
# # while left < right:
# #     temp = data[left] + data[right]
# #     if temp > x:
# #         right -= 1
# #     elif temp < x:
# #         left += 1
# #     else:
# #         # 조건만족
# #         result += 1
# #         # print('답:',data[left],data[right])
# #         left += 1
        
# # print(result)

