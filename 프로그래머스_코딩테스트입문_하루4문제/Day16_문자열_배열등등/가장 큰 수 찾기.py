'''
날짜: 2022.12.22
시간복잡도:

문제:
풀이:
23:38~23:41(3분)
[가장 큰 수, 그 수의 인덱스]
'''
def solution(array):
    return [max(array),array.index(max(array))]
    
def solution(array):
    max_value = -1
    max_index = -1
    for idx,i in enumerate(array):
        if i > max_value:
            max_value = i
            max_index = idx
    return [max_value, max_index]