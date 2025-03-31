'''
날짜: 2025.03.31
링크: https://leetcode.com/problems/top-k-frequent-elements/description/
시간복잡도: O(NlogN)

0.풀이예측
카운팅된 수를 저장할 수 있는 배열을 만든다.O(N)
카운팅이 많이된순서대로 정렬한다.O(NlogN)
k만큼 리스트에 넣어 반환한다. O(N)

1.학습키워드

2.문제

3.어떤 문제가 있었고, 나는 어떤 시도를 했는지
  
4.어떻게 해결했는지
  
5.무엇을 새롭게 알았는지

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        result = []
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
        
        sorted_nums = sorted(nums_dict.items(), key=lambda x:x[1])
        #print(sorted_nums)
        for i in range(k):
            a = sorted_nums.pop()
            result.append(a[0])
        #print(result)
        return result