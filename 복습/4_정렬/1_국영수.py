'''
1. 국어점수 감소하는 순
2. 영어점수 증가하는 순
3. 수학점수 감소하는 순
4. 다 같으면 이름을 사전 순
-> sorted() 정렬조건 설정 가능.

s_array = sorted(array,key= lambda x: (-x[1],x[2],-x[3],x[0]))
index = 1 인자를 기준으로 내림차순 정렬을 먼저 한다.
그 결과를 가지고 index = 2 인자를 기준으로 오름 정렬(-를 붙이면 내림차순 정렬) ...
'''
##########################################
##########################################
# 입력받는 형식 수정
n = int(input())
array = []
for i in range(n):
    array.append(input().split())

# 국어점수 내림차순으로 정렬함
s_array = sorted(array,key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in s_array:
    print(i[0])
##########################################
##########################################
# 나
n = int(input())
array = []
for i in range(n):
    name, kor, eng, math = map(str, input().split())
    array.append((name, int(kor), int(eng), int(math)))

# 국어점수 내림차순으로 정렬함
s_array = sorted(array,key= lambda x: (-x[1],x[2],-x[3],x[0]))
for i in s_array:
    print(i[0])

