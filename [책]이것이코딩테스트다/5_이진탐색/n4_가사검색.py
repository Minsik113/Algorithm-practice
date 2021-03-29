# from bisect import bisect_left, bisect_right

# def count_by_range(a, left_value, right_value):
#     left_index = bisect_left(a, left_value)
#     right_index = bisect_right(a, right_value)
#     return right_index - left_index

# def solution(words, queries):
#     answer = []
#     array =[[] for _ in range(10001)]
#     reversed_array = [[] for _ in range(10001)]
    
#     for word in words:
#         array[len(word)].append(word) # 단어 삽입
#         reversed_array[len(word)].append(word[::-1])
    
#     # 이진탐색을 해야하니까 각 리스트를 정렬한다.
#     for i in range(10001):
#         array[i].sort()
#         reversed_array[i].sort()

#     for q in queries: # 쿼리를 하나씩 보면서 수행한다.
#         if q[0] != '?': # 접미사에 '?'붙음
#             res = count_by_range(array[len(q)], q.replace('?','a'), q.replace('?','z'))
#         else: # 접두사에 '?' 붙음
#             res = count_by_range(reversed_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
#         answer.append(res)
    
#     return answer

# # 효율성 2개틀림.
# '''
# 찾는 단어수(10만) x 찾을곳(10만) = 너무많음. 
# 10만 x O(log(len(words)))으로 줄여야함.
# (array리스트 => words에 queries[i] 가 들어있는 단어들의 총 개수를 저장)

# 1번. words를 일단 정렬한다. 200만안됨.
# 단어길이 오름차순, 알파벳순 오름차순
# 2번. queries에서 단어 꺼내서 비교하자
# 3번. "찾는 단어의 길이"에 해당하는 '시작index' 와 '끝index'을 찾는다.
# 4번. 3번이 존재한다면 대입해서 하나씩본다
# 4-1번. 하나라도 다르면 다른것임.
# 5번. 3번이 존재안하면 0 리턴
# '''
# from bisect import bisect_left, bisect_right

# # target과 같은 길이의 시작index와 끝index를 찾는다. (이때, 끝index는 -1 해야함)(다음위치기 때문에)
# def find_index(array, length):
#     left_index = bisect_left(array, length)
#     right_index = bisect_right(array, length)
#     return (left_index, right_index)
    
# def solution(words, queries):
#     answer = []
#     # 1번. (길이, 사전)순서
#     words = sorted(words, key=lambda x:(len(x),x))
#     tree = dict() # 한번 본애들은 여기에 저장해두자.
#     sub_tree = dict() 
#     # 단어의 길이만 저장된 리스트 생성
#     array = []
#     for i in words:
#         array.append(len(i))
#     # print(words)
#     #2번. 단어 찾아보자 (queries에서 words안에 있는지 찾는것이다.)
#     for name in queries:
#         count = 0 # 단어가 몇개나 같은지 체크
#         # 3번. "찾는 단어의 길이"에 해당하는 '시작index' 와 '끝index'을 찾는다.
#         if name in sub_tree: # ------효율성 증가시키려고 사전에 봤던거 저장해둠
#             l_index, r_index = sub_tree[name]
#         else:
#             l_index, r_index = find_index(array, len(name))
#             sub_tree[name] = (l_index,r_index)
#         # 5번. 찾고자 하는 단어의 길이가 없다.
#         if r_index - l_index == 0: 
#             answer.append(0)
#         # 4번. 찾고자 하는 단어의 길이가 있다.
#         else:
#             # 4-1번. '해당 범위 안에 같은 문자가 있나' 체크한다
#             if name in tree: # ------효율성 증가하기위해 사전에 봤던거 저장해둠
#                 answer.append(tree[name])
#             else:
#             # name이 words안에 있는지 체크. (words = 길이오름차순, 사전순)
#                 for i in range(l_index, r_index, 1): # l_index ~ r_index-1 까지의 words안에 수를 본다
#                     flag = True # 다른문자있다면 False
#                     for j in range(len(name)):
#                         if name[j] == '?': # 무조건 같음
#                             continue
#                         if name[j] != words[i][j]: # 다르다면 다음 words랑 비교해본다
#                             flag = False
#                             break
#                     # words[i]와 name이 같다면) 개수 센다. 다음 문자 확인하러가자.
#                     if flag == True: 
#                         count+=1
#                 answer.append(count)
#                 tree[name] = count
    
#     return answer