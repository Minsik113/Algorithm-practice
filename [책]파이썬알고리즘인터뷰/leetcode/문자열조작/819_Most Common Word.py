##########################################
##########################################
# 4/3 - 정규식사용 전처리
import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        print(list(re.sub(r'[^\w]', ' ', paragraph).lower().split() ))
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                .lower().split()
                    if word not in banned]
        print(words)
        counts = collections.Counter(words)
        print(counts)
        return counts.most_common(1)[0][0]

##########################################
##########################################
# 4/3 - 첫풀이 앞부터 string하나씩보며 전처리
# '''
# 1. 단어마다 횟수 저장 ->dict()
# 2. 개수 기준 내림차순정렬
# 3. banned list에 없으면 출력
# '''
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         temp = ""
#         word_dictionary = dict()
        
#         for char in paragraph:
#             if char.isalpha():
#                 temp += char.lower()
#             else:
#                 temp = temp.lower()
#                 if temp not in word_dictionary:
#                     word_dictionary[temp] = 1
#                 else:
#                     word_dictionary[temp] += 1
#                 temp = "" # initailize
#         # 남은 temp를 검사해봐야함
#         s = ""
#         for char in temp:
#             if char.isalpha():
#                 s += char
#         try:
#             word_dictionary[s] += 1
#         except:
#             word_dictionary[s] = 1
            
#         print(word_dictionary)
        
#         # 추가된 예외값 넣어준다
#         plus = ''
#         banned.append(plus)
#         sort_dict = sorted(word_dictionary.items(), key = lambda x: x[1], reverse=True)
        
#         #
#         for word, _ in sort_dict:
#             if word not in banned:
#                 return word
        
