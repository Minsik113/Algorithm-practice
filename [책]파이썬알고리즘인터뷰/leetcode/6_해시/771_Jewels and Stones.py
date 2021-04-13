######################################
######################################
# 4/13 
from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 4. 파이써닉하게 풀기
        return sum([s in jewels for s in stones])
        # return sum(s in jewels for s in stones) 대괄호빼도 됨.
        
        # 3. Counter()
#         answer = 0
#         tree = Counter(stones)

#         # 존재 하지 않는 값들은 0으로 출력해줘서 아래와같은 코드 가능
#         for char in jewels:
#             answer += tree[char] 
#         return answer
        
        # 2-1. dict() 간결하게
#         answer = 0
#         tree = collections.defaultdict(int)
        
#         for char in stones:
#             tree[char] += 1
        
#         for char in jewels:
#             answer += tree[char]
        
#         return answer
        
        # 2. dict()
#         answer = 0
#         tree = dict()
        
#         for char in stones:
#             if char not in tree:
#                 tree[char] = 1
#             else:
#                 tree[char] += 1
        
#         for char in jewels:
#             if char in tree:
#                 answer += tree[char]
        
#         return answer
        
        
        # 1.set()
#         tree = set()
#         answer = 0
#         for char in jewels:
#             tree.add(char)
        
#         for char in stones:
#             if char in tree:
#                 answer += 1
#         return answer
            