'''
그리디
1. 각 행의 가장 작은 수를 뽑아 array리스트에 저장한다. heapq
2. array리스트의 max값 출력.
'''
##########################################
##########################################
# min저장 0.409s
import time
n, m = map(int, input().split())
start_time = time.time()
max_value = 0
for _ in range(n):
    save = list(map(int, input().split()))
    max_value = max(max_value, min(save))
end_time = time.time()
print(max_value)
print(end_time-start_time)


##########################################
##########################################
# 단순풀이 0.405s
# n, m = map(int, input().split())
# start_time = time.time()
# array = []
# for _ in range(n):
#     save = list(map(int, input().split()))
#     array.append(min(save))
# end_time = time.time()
# print(max(array))
# print(end_time-start_time)


