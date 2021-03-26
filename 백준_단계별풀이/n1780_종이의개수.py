'''
nxn  -1 0 1 중 하나

-> 재귀써야함
array = nxn 
1. check(array)해서 모든 수가 같은지 본다
2. 같으면 끝
3. 다르면 9등분해서 각부분의 리스트를 check(new_array)한다.
'''

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

a = 0
b = 0
c = 0

# array의 원소를 본다. 다르면 9 등분함
# 같으면 return
count = [0] * 3 # -1, 0, 1 을 저장
def check(array):
    global count
    flag = True
    print('---')
    print(array)
    # 모든값이 같은지 본다
    pre = array[0][0]
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] != pre:
                flag = False
    # 모두 같을때
    if flag:
        count[pre-1] += 1
        return
    # 하나라도 다를때 -> 9등분 각각을 재귀로 보낸다
    else:
        length = len(array) // 3
        print(array[0:length][0:length])
        print(array[length:2*length][0:length])
        print(array[2*length:3*length][0:length])
        print('--')
        print(array[0])
        print(array[0][:length])
        print(array[0][length:2*length])
        print(array[0][2*length:3*length])
        # check(array[0:length][0:length])
        # check(array[length:2*length][0:length])
        # check(array[2*length:3*length][0:length])

        # check(array[0:length][length:2*length])
        # check(array[length:2*length][length:2*length])
        # check(array[2*length:3*length][length:2*length])

        # check(array[0:length][2*length:3*length])
        # check(array[length:2*length][2*length:3*length])
        # check(array[2*length:3*length][2*length:3*length])

check(data)
# print(count)