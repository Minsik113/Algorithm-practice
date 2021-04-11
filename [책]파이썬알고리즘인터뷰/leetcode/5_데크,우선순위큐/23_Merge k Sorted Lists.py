##########################################
##########################################
# 4/11 - 서적코드 
# # -> 왜 저렇게 표현했는지 잘 이해가안간다. 다시 볼 때 집중해서 ㄱㄱ.

# import heapq

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         root = result = ListNode(None)
#         h = []
        
#         for i in range(len(lists)):
#             if lists[i]:
#                 heapq.heappush(h, (lists[i].val, i, lists[i]))
        
#         while h:
#             node = heapq.heappop(h)
#             idx = node[1]
#             result.next = node[2]
            
#             result = result.next
#             if result.next:
#                 heapq.heappush(h, (result.next.val, idx, result.next))
        
#         return root.next
            
##########################################
##########################################
# 4/11 - 첫풀이
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for array in lists:
            while True:
                if not array: # 비어있으면 넘어간다.
                    break
                heapq.heappush(h, array.val)
                array = array.next
        
        head = ListNode()
        temp = head
        while h:
            x = heapq.heappop(h)
            temp.val = x
            if not h:
                return head
            temp.next = ListNode()
            temp = temp.next