# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # 2. 각 방향의 곱셈합을 구한다.
#         result = []
#         p = 1
#         for i in range(0, len(nums)):
#             result.append(p)
#             p = p * num[i]
#         p = 1
#         # 왼쪽 곱셈결과에 오른쪽 값을 차례로 곱한다.
#         for i in range(len(nums) - 1, 0 - 1, -1): # 맨뒤~처음까지 1칸씩 거꾸로 간다.
#             result[i] = result[i] * p
#             p = p * nums[i]
#         return result    
        
#         # 1. 나눗셈 사용 - 나눗셈은 사용하면 안됨
# #         total = 1
# #         # 0인곳을 체크해둘까?
# #         zero_length = 0
# #         for i in range(len(nums)):
# #             if nums[i] == 0:
# #                 zero_length += 1
# #             else:
# #                 total *= nums[i]
        
# #         # 예외처리 -> 0이 2개이상이라면 모두 0 이다.
# #         result = []
# #         if zero_length >= 2:
# #             return [0 for _ in range(len(nums))]
        
# #         # 0이 1개 있다면
# #         elif zero_length == 1:
# #             for i in range(len(nums)):
# #                 if nums[i] == 0:
# #                     result.append(total)
# #                 else:
# #                     result.append(0)
# #         # 0이 없다면
# #         else:
# #             for i in range(len(nums)):
# #                 result.append(total//nums[i])
            
# #         return result
            