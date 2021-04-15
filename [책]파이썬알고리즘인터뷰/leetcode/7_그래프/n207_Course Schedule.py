'''
모르겟네
'''

# '''
# pre = [a,b]
# a를 듣기위해서 b를 먼저 들어야한다
# union-find해서 cycle생기면 False

# 그냥 위상정렬식으로 ingrdee 0 인거부터쭉보다가 cycle생기면 false
# '''
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
#         graph = collections.defaultdict(list)
#         # 그래프 구성
#         for x, y in prerequisites:
#             graph[x].append(y) # x를듣기위해서 y를 들어야함
        
#         traced = set()
        
#         def dfs(i):
#             # 순환구조이면 False
#             if i in traced:
#                 return False
            
#             traced.add(i)
#             for y in graph[i]:
#                 if not dfs(y):
#                     return False
            
#             # 탐색 종료 후 순환노드 삭제
#             traced.remove(i)
            
#             return True
            
        
#         # 순환 구조 판별
#         for x in list(graph):
#             if not dfs(x):
#                 return False
#         return True
            
    
    
    
    
    
    