##########################################
##########################################
# 4/2 - sort()
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # group digits or letters
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        # lambda expression
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

##########################################
##########################################
# 4/2 - 첫 풀이. 직접 하나씩 보고 합쳐서 출력,,
# 파이썬스럽지 못한 풀이...
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         # 
#         strings = []
#         numbers = []
#         for log in logs:
#             temp = list(log.split())
#             k = temp[1:]
#             if k[0].isalpha():
#                 strings.append((k, temp[0]))
#             else:
#                 numbers.append((k, temp[0]))
#         print(strings)
#         print(numbers)
#         strings = sorted(strings)
#         # numbers = sorted(numbers)
#         print(strings)
#         print(numbers)
        
#         # len(strings) + len(number)
#         # result = [""] * len()
#         result = []
#         for content, name in strings:
#             k = ""
#             k += name+" "
#             k += " ".join(content)
#             print(k)
#             result.append(k)
            
#         for content, name in numbers:
#             k = ""
#             k += name+" "
#             k += " ".join(content)
#             result.append(k)
        
#         return result
        