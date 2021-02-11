# 1/14
# 문제 유형: 해시, 배열, 구현
# 추천 풀이 시간: 20분

# 특정 정수의 등장 여부만을 간단히 체크하자
# dict 자료형을 해시처럼 사용가능
# 해당 문제는 set 자료형으로 간단히 해결됨
# set() = 집합. 중복x

n = int(input())
n_list = list(map(int, input().split(' ')))

m = int(input())
m_list = list(map(int, input().split(' ')))

for i in range(m):
    if m_list[i] in n_list: 
        print(1)
    else:
        print(0)

# 동빈나

n = int(input())
arr = set(map(int, input().split(' ')))
m = int(input())
x = list(map(int, input().split(' ')))

for i in x:
    if i not in arr:
        print(0)
    else:
        print(1)




