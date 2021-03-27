'''
n = 50만

1. dict()에 넣고 있나없나 체크
N개 데이터 넣고, M개데이터를 확인함
O(N + M)

2. 이진탐색 -> n=50만이니까 90x50만 = 4500만.ㄷㄷ
N개데이터 정렬하고 M개데이터 확인함
1개 데이터 찾는데 O(logN) M개니까 MlogN
O(NlogN + MlogN) 
O( (M+N)logN )
'''
##########################################
##########################################
# 1. dict()
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
m = int(input())
array = list(map(int, input().split()))

tree = dict()
for i in data:
    try:
        tree[i] += 1
    except:
        tree[i] = 1
for i in array:
    try:
        print(tree[i], end=' ')
    except:
        print(0, end=' ')
# # dict()에 넣자
# tree = dict()
# for i in range(n):
#     if str(data[i]) not in tree:
#         tree[str(data[i])] = 1
#     else:
#         tree[str(data[i])] += 1

# # dict()에서 찾자
# for i in range(m):
#     if str(array[i]) in tree:
#         print(tree[str(array[i])], end=' ')
#     else:
#         print(0, end=' ')