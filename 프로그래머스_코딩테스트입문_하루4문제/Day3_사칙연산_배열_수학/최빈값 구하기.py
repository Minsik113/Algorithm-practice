'''
Counter쓰는거 익혀보자

from collections import Counter

Counter(array).most_common() # 이거하면 "문자":빈도수 로 나옴

'''

def solution(array):
    num_dict = dict()
    num_set = set()
    # 빈도수 저장
    for i in array:
        if i not in num_dict:
            num_dict[i] = 1
            num_set.add(i)
        else:
            num_dict[i] += 1
    
    temp = max(num_dict.values())
    cnt = 0
    answer = -1
    for i in num_set:
        if num_dict[i] == temp:
            cnt += 1
            answer = i
            
    if cnt != 1:
        return -1
    
    return answer
