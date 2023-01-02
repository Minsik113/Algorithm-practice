'''
날짜: 2023.01.01
시간복잡도:

문제:
spell안에 있는 알파벳을 딱 '한 번'씩 사용해서 만든 단어가 존재하는가? (존재 1, 존재x 2)

풀이:
10:48~11:01(13분)
방법2.
set활용

방법1.
0. spell 사전 선언. spell_dict
1. 단어를 앞부터 보면서 카운트
2. 단어가 끝났을 때, spell_dict를 봐서 모두 1인지 확인 
'''
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s): # 모두 겹치면 존재
            return 1
    return 2
    
def solution(spell, dic):
    answer = 1
    check = len(spell)
    
    for word in dic:
        temp = 0 
        for i in spell:
            a = word.count(i)
            if a != 1: # 이 단어는 더 이상 안봄. 다음 단어로 넘어가자
                break
            else:
                temp += 1
        if temp == check:
            return 1
    return 2