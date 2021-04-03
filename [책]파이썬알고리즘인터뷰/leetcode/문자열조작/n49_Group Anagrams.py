# '''
# 같은 수, 같은 문자들로 구성된 애들끼리 묶어라
# 각단어들을 정렬해서 이미 있는지 체크하면서 묶는다.
# '''
# import collections

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = collections.defaultdict(list)
        
#         for word in strs:
#             # 정렬해서 dict에 추가
#             anagrams[''.join(sorted(word))].append(word)
#         return anagrams.values()
        
                
        