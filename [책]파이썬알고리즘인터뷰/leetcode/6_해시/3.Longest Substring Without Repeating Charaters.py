# ##########################################
# ##########################################
# # 4/13 - 
# # 2. 슬라이딩 윈도우, 투포인터 -> 2회독때 다시
# # 맨처음 풀려고 시도했던 방법이 '슬라이딩 윈도우'네
from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. 내풀이 - set, deque로 풀기
        max_value = -int(1e9)
        charset = set()
        q = deque()
        
        for char in s:
            # 1. dict에 없을 때 -> set추가, queue늘리기
            if char not in charset:
                charset.add(char)
                q.append(char)
            
            # 2. dict에 있을 때
            else:
                max_value = max(max_value, len(q)) # 최대길이 저장
                q.append(char) # 중복된값 넣어주고
                while True: # 중복된값 찾는다.
                    if q[0] == char:
                        q.popleft()
                        break
                    else:
                        charset.remove(q.popleft())
        max_value = max(max_value, len(q))
        
        return max_value
                
# from collections import deque

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # 2. 슬라이딩윈도우, 투포인터.
#         used = dict()
#         max_length = start = 0
#         for index, char in enumerate(s):
#             # 이미 등장해던 위치라면 'start'위치 갱신
#             if char in used and start <= used[char]:
#                 start = used[char] + 1
            
#             # 최대 부분 문자열 길이 갱신
#             else:
#                 max_length = max(max_length, index - start + 1)
            
#             # 현재문자의 위치 삽입
#             used[char] = index
            
#         return max_length
        

        
        
                
                
                