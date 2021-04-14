class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # 2. 1번을 간략하게 - 1보다 더빠름
        result = []
        def dfs(csum, index, path):
            # 종료조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            # 자신부터 하위 원소 까지의 나열 - 재귀호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
        
        dfs(target, 0, [])
        return result
        
        # 1. 백트래킹
#         # target값보다 작은것들만 골라보자
#         array = []
#         for i in candidates:
#             if i <= target:
#                 array.append(i)
        
        
#         # array애들을 중복해가면서 n개뽑아서 target이 되게 만들어보자
#         results = []
        
#         def check(now_value):
#             if now_value > target:
#                 return False
#             return True
        
#         def dfs(s, start, now_value):
#             if now_value == target:
#                 results.append(s[:])
#                 return
            
#             for i in range(start, len(array)):
#                 t = array[i]
#                 s.append(t)
#                 now_value += t
#                 if check(now_value):
#                     dfs(s, i, now_value) # 더 작은값은 안보려고
#                 s.pop()
#                 now_value -= t
                
            
#         dfs([], 0, 0)
#         return results
        