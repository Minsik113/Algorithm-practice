'''
날짜: 2023.01.05
시간복잡도:

문제:
풀이:
16:19~16:39 모르겟다
1. 각각의 길이에 대한 숫자를 리스트에저장
2. 리스트를 정렬해서 2개 이상 나온 숫자의 개수

'''
def solution(lines):
    answer = 0
    temp = dict()
    for a,b in lines:
        for i in range(a,b+1):
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
    final = []
    for key,val in temp.items():
        if val >= 2:
            final.append(key)
    print(final)
    if len(final) <= 1: # 예외처리
        return 0
    prev = final[0]
    total = []
    test = [prev]
    flag = False # 마지막 값을 넣었는가
    for i in range(1,len(final)):
        if final[i] == prev + 1: # 연속된 숫자라면
            prev = prev+1 # 현재값이 prev가 된다.
            test.append(prev)
            flag = False
        else: # 연속된 숫자가 아니라면
            total.append(test) # 임시저장하고,
            test = [final[i]]
            flag = True
        
    if not flag or len(test)==1:
        total.append(test)
    print(total)
    for s in total:
        print(len(s),s)
        if len(s)!=1: # 선분이라면
            answer += s[-1] - s[0]
    return answer