# 1/12 프린터 큐 1966번
# queue - FIFO
# 중요도 체크해서 제일 중요하면 출력. 아니라면 맨 뒤로.
# 중요도: 숫자 클수록 중요함.
# A B C D: 2 1 4 3 이라면 C D A B 순서로 출력
# 그냥 제일 중요한애 먼저 출력
# N개의 문서
# a번째로 인쇄된 문서는 현재 QUEUE에서 b번째에 노

# 1. 데이터 개수가 많지않음. N<=100이니까 요구하는 대로 구현한다.
# 2. 리스트에서 가장 큰 수가 앞에 올 때까지 회전시킨 뒤 추출.
# 3. 가장 큰 수가 M이면서 가장 앞에 있을 때 프로그램을 종료한다.'

n = int(input())

queue = []
answer = []

for _ in range(0,n): # n번 볼것이다.
    num, index = list(map(int, input().split(' '))) # 문서개수, 궁금한 문서순서
    data = list(map(int, input().split(' '))) # 중요도
    data = [(i, idx) for idx, i in enumerate(data) ] # (중요도, 고유숫자)
    
    count = 0

    while True:
        # max()로 중요도가 제일높은 튜플(a,b)가 맨앞임. a를 볼거니까 [0]
        if data[0][0] == max(data, key=lambda x:x[0])[0]: 
            count += 1
            if data[0][1] == index:
                print(count)
                break
            else:
                data.pop(0)
        # 맨 뒤로 보낸다.
        else:
            data.append(data.pop(0))



# 동빈나

# 1/12 프린터 큐 1966번
# enumerate(list)이용 = 튜플형태로 만들어줌
#  특정한 list를 각각 index랑 같이 파악할 수 있도록 묶어줌

test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    ee = list(map(int, input().split(' ')))
    data = [(i, idx) for idx, i in enumerate(ee)] # (중요도, 숫자)
        # [(2,0), (1,1), (4,2), (3,3)] (중요도, 숫자)
    count = 0

    while True:
        if data[0][0] == max(data, key=lambda x: x[0])[0]:
            count += 1
            if data[0][1] == m: # 내가 선택했던 애라면 인쇄하고 break
                print(count)
                break
            else:
                data.pop(0)
        else:
            data.append(data.pop(0))


