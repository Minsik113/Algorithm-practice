


# '''
# dfs로 들어있는 값들중 작은애를 따라가라
# '''
# import heapq
# from collections import defaultdict, deque
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
#         # 3. 일정 그래프 반복
#         graph = defaultdict(list)
        
#         for a, b in sorted(tickets):
#             graph[a].append(b)
            
#         result, stack = [], ['JFK']
#         while stack:
#             # 반복으로 스택을 구성, 도로가 없는 곳에서 풀어낸다.
#             while graph[stack[-1]]: 
#                 stack.append(graph[stack[-1]].pop(0))
#             result.append(stack.pop())
#         return result[::-1]
        
#         # 2. 스택으로 1번을 개선함
# #         edges = defaultdict(list) # value값들이 []임
        
# #         for start, end in sorted(tickets, reverse=True):
# #             edges[start].append(end)
        
# #         result = []
# #         def dfs(v):
# #             # 마지막 값을 읽어 어휘 순 방문
# #             while edges[v]:
# #                 dfs(edges[v].pop()) 
# #             result.append(v)
        
# #         dfs('JFK')
# #         return result[::-1]
        
#         # 1. dfs일정 재구성
# #         edges = defaultdict(list) # value가 리스트임
        
# #         for start, end in sorted(tickets):
# #             edges[start].append(end)
        
# #             # tickets를 sort시키는것으로 아래코드를 안써도 됨
# #             # # edges[i]에 들어있는 값들을 알파벳순으로 정렬
# #             # for key, value in edges.items():
# #             #     edges[key].sort()
        
# #         result = []
        
# #         def dfs(v):
# #             while edges[v]:
# #                 dfs(edges[v].pop(0)) # 맨앞이 어휘순으로 먼저니까
# #             result.append(v)
        
# #         dfs('JFK')
# #         return result[::-1]
            
        
        