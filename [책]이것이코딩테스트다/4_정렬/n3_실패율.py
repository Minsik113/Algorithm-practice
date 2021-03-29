##########################################
##########################################
# 3/4 복습 
# dict()에 실패율 저장
def solution(N, stages):
    result = dict()
    # 1번. stages에 사람 몇명이나 있는지 확인
    number_list = [0] * (N+2)
    length = 0 # 총원 저장
    for i in stages:
        number_list[i] += 1
        length += 1
    # 2번. 실패율 계산
    for stage in range(1, N+1):
        if length != 0:
            result[stage] = number_list[stage] / length
            length -= number_list[stage]
        else:
            result[stage] = 0
    
    return sorted(result, key=lambda x:result[x], reverse=True)
##########################################
##########################################
# 3/4 복습 
# []에 실패율저장
'''
실패율 = 스테이지에 도달했으나 아직클리어 못한 플레이어수 / 스테이지에 도달한 플레이어 수
-> 실패율이 높은것부터 내림차순으로 스테이지 번호 리턴
(단, 실패율 같으면 '스테이지 번호 낮은 것'부터)
20만 -> 계수정렬사용해야함. 

1. 각 스테이지에 몇 명이 있는지 저장하는 리스트 count_num
2. 실패율 저장할 리스트 fail_list에서 실패율 계산하고, 총원수정(총원(N) - count_num[i])

'''
def solution(N, stages):
    answer = []
    fail_list = [] # 실패율 저장
    count_num = [0] * (N+2) # 0~N+1까지
    total = 0 # 총원
    # 1번. 각 스테이지에 몇명이 있는가
    for i in stages: 
        count_num[i] += 1
        total += 1
    
    # 2번. 실패율 계산하자
    for i in range(N+2):
        if total == 0: # 나머지 뒤에 실패율을 0 으로 넣는다.
            for j in range(i,N+2):
                fail_list.append((0,j))
            break
        fail_list.append((count_num[i] / total, i)) # (실패율,스테이지번호)
        total -= count_num[i]
    # 3번. 1번~N번까지 실패율 순서로 정렬
    s = sorted(fail_list[1:-1], key=lambda x:(-x[0],x[1])) #실패율내림차순, 실패율같으면 스테이지오름차순
    answer = [i[1] for i in s]
    return answer
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
