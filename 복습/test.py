from bisect import bisect_left, bisect_right

def search(data, m):
    left_index = bisect_left(data, m)
    right_index = bisect_right(data, m)
    print(left_index, right_index)
    return right_index - left_index

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = search(data,m)
if result == 0: # 값이 없음
    print(-1)
else:
    print(result)