'''
'''
def solution(N, stages):
    answer = []
    # 1. 사용자마자 어디 스테이지를 도전중인지 체크하자
    check = [0] * (N+2) # check[i] = i번째 스테이지에 있는사람 check[N+2] = 다깬사람
    percentage = [0] * (N+2)
    for i in stages:
        check[i] += 1
    user_num = sum(check)
    
    # 2. 실패율 계산하자
    result = []
    for i in range(1, N+1): # 1~ N단계까지 (N+1은 안봐도됨)
        if user_num != 0:
            percentage[i] = check[i] / user_num
            user_num -= check[i]
        result.append((percentage[i],i)) # (실패율, 스테이지)
    print(result)
    # 3. 실패율의 내림차순 정렬
    # result.sort(key=lambda x:x[0], reverse=True) # 정렬되어있는상태에서 조건대로 정렬하는거니까 자동정렬됨
    result.sort(key=lambda x:(-x[0],x[1]))
    for i in result:
        answer.append(i[1])
    
    return answer
##########################################
##########################################
# 
def solution(N, stages):
    answer = []
    length = len(stages)
    # 1. 각 스테이지에 몇명이 있는가
    for i in range(1,N+1):
        # 해당 스테이지에 머물러 있는 사람 수
        count = stages.count(i)
        fail = 0
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        # (스테이지번호,실패율)
        answer.append((i,fail))
        length -= count
    
    # 3. 정렬 시작
    answer = sorted(answer, key=lambda x:(-x[1],x[0]))
    # s_array = sorted(stage_total, key=lambda x:(-x[1],x[0])) # 스테이지 실패율(내림차)순. 같으면 숫자오름차순
    result = [i[0] for i in answer]
    return result
##########################################    
##########################################
# 풀이형식 거의 같음. 왜 난 런타임 에러났지?? 시간인가? 모르겟네
# => n=5, starges=[2] result=[2,1,3,4,5]나와야하는데 이렇게하면result=[2,1]만나옴

# def solution(N, stages):
#     answer = []
#     stage_count = [0] * (N+1) # i 스테이지 꺤 사람들 수. (단, 다 깬 사람은 무시)
#     stage_total = []
#     # 1. 각 스테이지에 몇명이 있는가
#     for i in stages:
#         if i > N: # 다꺤사람은 뻄.
#             continue
#         stage_count[i] += 1
        
#     # 2. (스테이지, 실패율) 정리
#     total = len(stages) # 총 사람수
#     for i in range(1, N+1):
#         if total == 0: # 0으로 나눌 수 없다. 스테이지는 많은데 그전에 사람들 다 끝날 수도 있다.
#             stage_tatal.append((i,0))
#         else:
#             stage_total.append((i,stage_count[i] / total)) # (stage,실패율)
#             total -= stage_count[i]
#     # 3. 정렬 시작
#     print(stage_count)
#     print(stage_total)
#     s_array = sorted(stage_total, key=lambda x:(-x[1],x[0])) # 스테이지 실패율(내림차)순. 같으면 숫자오름차순
#     for i in s_array:
#         answer.append(i[0])
#     print(answer)
#     return answer
