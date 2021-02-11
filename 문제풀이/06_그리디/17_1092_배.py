'''
# 1/31
# 문제 난이도: Gold 5
# 문제 유형: 그리디
# 추천 풀이 시간: 35분

모든 박스를 배로 옮기는데 드는 시간의 최솟값을 계산
매 분마다, 모든 크레인에 대하여 옮길 수 있는 박스를 선택하여 옮긴다.
박스를 무게 기준으로 '내림차순 정렬'한 뒤에, 무거운것부터 옮기자.
O(NM) 
https://velog.io/@ju_h2/Python-%EB%B0%B1%EC%A4%80-1092.-%EB%B0%B0-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%83%90%EC%9A%95-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B7%B8%EB%A6%AC%EB%94%94-%EA%B5%AC%ED%98%84-5
'''

n = int(input()) # 크레인 수
cranes = list(map(int, input().split()))
m = int(input()) # 박스 수
boxs = list(map(int, input().split())) 

cranes.sort(reverse=True)
boxs.sort(reverse=True)

 # 못 옮김
if boxs[0] > cranes[0]:
    print(-1)
    exit()

positions = [0] * n # 각 크레인이 옮겨야하는 박스의 시작 번호 (0부터 시작)
checked = [False] * m
result = 0
count = 0

while True:
    if count == len(boxs): # 박스 다 옮겼다면 종료
        break
    for i in range(n): # 모든 크레인에 대하여
        while positions[i] < len(boxs):
            # 아직 안옮긴 박스중에서, 옮길 수 있는 박스 만날때까지 반복
            if not checked[positions[i]] and cranes[i] >= boxs[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1
print(positions)
print(result)



