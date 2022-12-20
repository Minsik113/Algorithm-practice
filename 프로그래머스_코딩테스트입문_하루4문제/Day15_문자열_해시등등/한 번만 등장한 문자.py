'''
날짜: 2022.12.20
시간복잡도: O(NlogN)

문제:
문자열에 한 번만 등장한 알파벳을 오름차순 sort해라

풀이:
16:48~16:53(5분)
방법1.set()으로 분류 O(N)
 없으면 add, 있으면 delete 
 출력해서 정렬. O(NlogN)
방법2.count()를 이용
'''
def solution(s):
    return ''.join(sorted([i for i in s if s.count(i)==1]))
    
def solution(s):
    dic = set() # 전체 사전 
    remove_list = set() # 제거해야할 리스트
    # 1. 알파벳 체크
    for i in s:
        if i in dic:
            remove_list.add(i)
        else:
            dic.add(i)
    # 2. 중복되는 문자 제거
    for i in remove_list:
        dic.remove(i)
    return ''.join(sorted(list(dic)))
