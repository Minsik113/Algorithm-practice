'''
10^3 x 10^3 하면 충분
1. 1~len(s) // 2에 대해 압축이 되나 본다.
-> len(s)의 반 까지의 길이로 압축해봄.
2. 리스트에 저장한길이중 짧은거 출력
'''
##########################################  
##########################################  
#
def solution(s):
    answer = int(1e9)
    length = len(s)
    if len(s)==1:
        return 1
    # 1번
    count = 1
    for plus in range(1,length//2+1): # 길이1 ~ 길이절반
        temp = ''
        for i in range(0,length,plus): # 
            # 1. 같으면 이어서본다.
            if s[i:i+plus] == s[i+plus:i+plus*2]: 
                # print(plus,'일때',s[i:i+plus])
                count += 1
            # 2. 같지않으면 그대로 문자열에 추가
            else: 
                if count == 1: # 겹치는게 없음
                    temp += s[i:i+plus]
                else: # 겹치는 횟수 만큼
                    temp += str(count) + s[i:i+plus]
                    count = 1
                    
        # print(temp)
        answer = min(answer, len(temp))
    
    return answer
##########################################  
##########################################  
#
def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 + 1):
        strings = ""
        prev = s[0:step] # 앞에서 step만큼의 문자열 추출
        count = 1
        for j in range(step,len(s),step):
            # 1번 같은 문자열이라면
            if s[j:j+step] == prev:
                count += 1
            # 2번 다른 문자열일 경우
            else:
                strings += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step] # 상태초기화
                count = 1
        # 남아있는 문자열 정리
        strings += str(count) + prev if count >= 2 else prev
        # 만들어지는 문자열중 짧은것이 정답
        answer = min(answer, len(strings))
    
    return answer