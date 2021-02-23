'''
완전탐색 -> 값 찾기?
N=10^3이다. 
1. 모든 조합 계산한다.
2. i개의 조합을 찾기전에 pos못찾으면 pos가 정답임.
-> 그다음은 최소한 pos보다 더 큰수가 제일 작은수이기 때문이다.
'''
# from itertools import combinations

# n = int(input())
# coins = list(map(int, input().split()))
# pos = 1 # 1원부터 없는 수 찾을것이다.
# coin_type = set()

# # 동전 넣어줌
# for i in range(len(coins)):
#     target = coins[i]
#     if target not in coin_type:
#         coin_type.add(target)

# # pos로 어디부터 찾을지본다
# for i in range(1, max(coins)): # 1부터 제일큰 코인값까지 없는위치찾는다.
#     if i not in coin_type:
#         pos = i
#         pos += 1
#         break

# # pos가 들어있어야함.
# flag = False
# while True:
#     if flag:
#         break
#     for i in range(2, n): # pos가 동전조합에 있으면 나옴.
#         print(list(combinations(coins, i)))
#         for j in list(combinations(coins, i)): # 2~n개로 조합 짤것이다.
#             value = sum(j)
#             if value not in coin_type:
#                 coin_type.add(value)
#         print('종류: ',coin_type)
#         print('찾는수:',pos)
#         if pos in coin_type: # pos가 있다면 연속된수가 어디까지있나봄.
            
#             break

# print('정답:',pos)
