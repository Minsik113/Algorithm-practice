'''
# 1/31
# 문제 난이도: Silver 5
# 문제 유형: 그리디
# 추천 풀이 시간: 20분

동빈
:모두 0으로 만드는 경우 vs 모두 1로 만드는 경우

민식
: 0->1 로 바꾸는 경우  1->0로 바꾸는경우 를 count리스트에 넣고
더 작은수를 출력한다.
'''

data = list(map(int, input()))
count = [0] * 2 # '0의 연속된 수', '1의 연속된 수' 세기위해서
count[data[0]] = 1

for i in range(1, len(data)):
    if data[i] == data[i-1]:
        continue
    else:
        count[data[i]] += 1
print(min(count))