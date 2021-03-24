##########################################
##########################################
# 3/24 - 오른쪽 or 왼쪽 비교할때 나보다 효율적으로 구함
'''
array.rotate(1) 맨뒤의값이 맨앞으로 온다
array.rotate(2) 맨뒤의값이 맨앞으로 온다 x 2
'양수'면 '뒤에있는걸 앞'으로 옮긴다.
'음수'면 '앞에있는걸 뒤'로 옮긴다.
'''
import sys
from collections import deque

n, _ = map(int, input().split())
numbers = list(map(int, input().split()))
q = deque(range(1, n+1))
total = 0

for idx in range(len(numbers)):
    # 1.
    if numbers[idx] == q[0]:
        q.popleft()
        continue
    q_idx = q.index(numbers[idx]) # number[idx]의 index를 찾아줌
    # 뒤 -> 앞 으로 옮기는게 유리한경우
    if q_idx > len(q) // 2:
        q.rotate(len(q) - q_idx)
        total += len(q) - q_idx
    # 앞 -> 뒤 로 옮기는게 유리한 겨웅
    else:
        q.rotate(-q_idx)
        total += q_idx
    q.popleft()
print(total)

##########################################
##########################################
# 3/24 - 내풀이
'''
왼쪽으로이동 array.append(array.popleft())
오른쪽으로이동 array.insert(0, array.pop())
Tip
왼쪽으로이동해야 빨리만나는지 오른쪽으로 이동해야 빨리만나는지체크
'''
# from collections import deque

# n, m = map(int, input().split())
# find_data = deque(list(map(int, input().split()))) # 찾을 값
# array = deque([i for i in range(1, n+1)])
# result = 0
# # print('시작',array)
# while find_data:
#     value = find_data.popleft() # 찾고자 하는값
#     # 0. 시작점이 찾는값이면 바로 빼주고 다음값본다
#     if array[0] == value:
#         array.popleft()
#         continue
#     # 1. 2번으로 갈 때 걸리는 횟수
#     count2 = 1 
#     for i in range(1, len(array)):
#         if array[i] == value:
#             break
#         count2 += 1
#     # 2. 3번으로 갈 때 걸리는 횟수
#     count3 = 1 # 거꾸로볼때는 이미 한칸 이동한상태로 봐야한다.
#     for i in range(len(array)-1, -1, -1):
#         if array[i] == value:
#             break
#         count3 += 1
#     # 3. count3쪽으로감
#     # 뒤에있는거 빼서 앞으로 보내고 값빼준다
#     if count2 > count3: 
#         result += count3
#         for _ in range(count3):
#             array.insert(0, array.pop())
#         array.popleft()
#     # 4. count2쪽으로감
#     # 앞에있는거빼서 뒤로 보내고 값 빼준다
#     else:
#         result += count2
#         for _ in range(count2):
#             array.append(array.popleft())
#         array.popleft()
#     # print('적용',array)
# # print('끝',array)
# print(result)



