'''
그리디

1. 0,1있으면 '+'
2. 없으면 '*' 하면된다.

-> 제일 큰 수 가능
'''
##########################################
##########################################
#
array = input()

result = int(array[0])
for i in range(1,len(array)):
    if int(result) <= 1 or int(array[i]) <= 1:
        result += int(array[i])
    else:
        result *= int(array[i])
print(result)

##########################################
##########################################
# 나
# array = list(map(int,input()))
# prev = array[0]

# for i in range(1, len(array)):
#     check = array[i]
#     if prev <= 1 or check <= 1:
#         prev = prev + check
#     else:
#         prev = prev * check
# print(prev)
