'''
# 1/31
# 문제 난이도: Gold 5
# 문제 유형: 그리디
# 추천 풀이 시간: 30분

최대 K개 집중국설치
목표 = 집중국들의 수신 가능 영역의 길이의 합을 최소화
사실상 정렬만 수행하면 되므로 O(NlogN)

k개의 영역으로 나눈거랑 같은말이다.
0/ 센서들을 오름차순 정렬한다.
1/ 각 센서 사이의 거리를 계산한다.
2/ 가장 거리가 먼 순서대로 K-1개의 연결고리를 제거한다
'''

n = int(input())
k = int(input())

if k >= n:
    print(0)
    exit()

array = list(map(int, input().split()))
array.sort()
distances = []

for i in range(1, n):
    distances.append(array[i]-array[i-1])

distances.sort(reverse=True)

for i in range(k-1):
    distances[i] = 0
print(sum(distances))