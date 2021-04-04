# 4/4 
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
        
        # 2.. brute force -> 시간초과
        # max_price = 0
        # for i, price in enumerate(prices):
        #     for j in range(i, len(prices)):
        #         max_price = max(max_price, prices[j] - price)
        # return max_price
        
        # 1. 처음풀이. 비효율적
#         length = len(prices)
#         # i일에 살 수 있는 제일 작은 값
#         dp1 = [0] * length
#         pre = int(1e9)
#         for i in range(length):
#             if prices[i] < pre:
#                 pre = prices[i]
#             dp1[i] = pre
        
#         # i일에 팔 때 제일 좋은 가격
#         sell = [0] * length
#         max_value = 0
#         for i in range(1, length):
#             temp = dp1[i-1] - prices[i]
#             if temp >= 0: # 비싸게사서 싸게팜. -> 안됨
#                 sell[i] = 0
#             else:
#                 max_value = max(max_value, -temp)
#                 sell[i] = -temp
                
#         print(sell)
#         return max_value