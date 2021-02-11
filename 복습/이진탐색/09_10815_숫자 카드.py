# 1/20
def Bsearchtree(array, target): # array에서 target값을 찾을것이다.
    start = 0   
    end = len(array)-1

    while start <= end :
        mid = (start + end) // 2

        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid +1
    
    return 0

import sys

n = int(sys.stdin.readline())
n_array = list(map(int, sys.stdin.readline().split(' ')))
m = int(sys.stdin.readline())
m_array = list(map(int, sys.stdin.readline().split(' ')))

n_array.sort()

result = []

# m_array에 있는것을 모두 확인해야함
for i in m_array:
    # 탐색시작
    result.append(Bsearchtree(n_array, i))

# print(result)
print(" ".join(map(str, result)))
# for i in m_list: 
#     # i 가 찾고자 하는 수
#     print(Bsearchtree(n_list, i), end=' ')
        

