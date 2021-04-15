class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # 2. dfs
        result = []
        
        def dfs(index, path):
            # 매번 결과 추가
            result.append(path)
            
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        
        dfs(0, [])
        return result
        
        # 1. 백트래킹구현
#         result = [[]]
        
#         # path길이가 length가 되면 저장
#         def backtracking(path, start, length):
#             if len(path) == length:
#                 result.append(path[:])
#                 return
            
#             for j in range(start, len(nums)):
#                 path.append(nums[j])
#                 backtracking(path, j+1, length)
#                 path.pop()
#             return
        
#         for i in range(1, len(nums)+1): 
#             backtracking([], 0, i) # i개로 이루어지 path
            
                
#         return result