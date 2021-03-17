##########################################
##########################################
# 3/17 복습
# 못품. ㅜㅜ

'''
1. G개의 배열만듦
2. P개의 비행기가들어옴

-> '번호가 가장 높은 탑승구'에 우선배치하며 이전에 들어갈 자리가 있는지본다.
G, P = 10^5이므로 O(NlogN)쪽으로 보게해야함

'''
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# n = int(input())
# p = int(input())

# # 부모 초기화
# parent = [0] * (n+1)
# for i in range(1, n+1):
#     parent[i] = i

# # 비행기를 탑승구에 넣는다.
# count = 0
# for _ in range(p):
#     k = find_parent(parent, int(input()))
#     # 못 들어가면 나옴
#     if k == 0:
#         break
#     # 들어갈 수 있으면 작은 탑승구와 합한다.
#     union_parent(parent, k, k-1)
#     count += 1

# print(count)

    