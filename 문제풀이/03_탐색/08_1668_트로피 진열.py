# 1/19
# 문제 난이도: Bronze 2
# 문제 유형: 탐색
# 추천 풀이 시간: 20분

####################### ####################### 
# 다시풀어본거 . 
def ascending(array):
    count = array[0]
    result = 1

    for i in range(1,len(array)):
        if count < array[i]:
            result += 1
            count = array[i]

    return result


x = int(input())
array = []

for _ in range(x):
    array.append(int(input()))

print(ascending(array))
#print(list(reversed(array)))
array.reverse()
print(ascending(array))
    
    
x = int(input())

list_tropy = []
idx = 0
l_count = 0
r_count = 0

for _ in range(x):
    list_tropy.append(int(input()))

for i in range(len(list_tropy)): # 5개
    if idx < list_tropy[i]:
        idx = list_tropy[i]
        l_count += 1

idx= 0

for i in range(len(list_tropy)-1,-1,-1):
    if idx < list_tropy[i]:
        idx = list_tropy[i]
        r_count += 1
print(l_count)
print(r_count)

 ####################### #######################   
# 동빈나

def ascending(array):
    now = array[0]
    result = 1
    for i in range(1,len(array)):
        if now < array[i]:
            result += 1
            now = array[i]
    return result

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

print(ascending(array))
reversed(array)
print(ascending(array))
    