'''
암호: L개의 알파벳
조건) 
1. 모음1개이상
2. 자음 2개이상
3. L개의 알파벳이 오름차순 

->
1/ 정렬해서 L개로 조합을 뽑으면되네.1
2/ 모음개수,자음개수 확인 
3/ 조건만족하는것만 출력

'''

##########################################
##########################################
# 백트래킹으로 구현
l, c = map(int , input().split())
array = list(map(str,input().split()))
array.sort()

vowel = 0 # 모음 수 
consonant = 0 # 자음 수
alpha = ['a','e','i','o','u'] 
result = []
strings = []

# 일단 L개로 이루어진 암호조합 생성
def dfs(depth, idx):
    if depth == l:
        result.append(''.join(strings))
        return
    for i in range(idx, c):
        strings.append(array[i])
        dfs(depth+1, i+1)
        strings.pop()

def check(result):
    for i in result:
        vow = 0 # 모음 수
        cons = 0 # 자음 수
        for j in i:
            if j in alpha:
                vow += 1
            else:
                cons += 1
        if vow >= 1 and cons >= 2:
            print(i)

dfs(0, 0)
check(result)

##########################################
##########################################
# itertool 사용
# import itertools

# l, c = map(int, input().split())
# array = list(map(str, input().split()))
# alpha = ['a','e','i','o','u'] # 모음

# array.sort()

# # 오름차순이니까 조합 뽑는다.
# save = []
# for i in itertools.combinations(array, l): # array를 l개씩 묶어 조합뽑음
#     save.append(list(i))

# # 모든 조합중 조건에 맞는암호 출력
# for data in save:
#     vowel = 0 # 모음 수
#     consonant = 0 # 자음 수

#     for j in range(l): # 모음 자음 확인
#         if data[j] in alpha:
#             vowel += 1
#         else:
#             consonant += 1
    
#     if vowel >= 1 and consonant >= 2:
#         print(''.join(map(str,data)))


