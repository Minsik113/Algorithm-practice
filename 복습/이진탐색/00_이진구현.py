'''
이진탐색
1. 재귀
2. 단순반복문
'''
##########################################
##########################################
# 1. 재귀 탐색
# 원소의개수, 찾고자하는 문자
# n, target = map(int, input().split())
# array = list(map(int, input().split()))

# def binarysearch_tree(array, target, start, end): # 배열, 찾는수, 시작, 끝
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif target < array[mid]: # 타겟이 작으니 끝점 줄임
#         binarysearch_tree(array, target, start, mid-1)
#     else:
#         binarysearch_tree(array, target, mid + 1, end)

# result = binarysearch_tree(array, target, 0, n-1) # result 인덱스에 있다.
# if result == None:
#     print("없음")
# else:
#     print(result,'위치에 존재한다.')

##########################################
##########################################
# 2. 단순 반복문
n, target = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = n-1
def binary_search_tree(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target: # 더 작은위치를 봐야함
            end = mid - 1
        else:
            start = mid + 1
    return None

result = binary_search_tree(array, target, 0, n-1)
if result == None:
    print("없음")
else:
    print('{}위치에 존재한다'.format(result))
