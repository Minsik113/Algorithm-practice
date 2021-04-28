plus_list = input().split('-')
print(plus_list)
result = 0

for i in plus_list[0].split('+'):
    result += int(i)

for i in plus_list[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)
# '''
# 55+50-50+40-50
# 55+50-(50+40)-50
# 그냥 쉽게생각하자.
# 1, -있으면 괄호 열고
#     -나오면 그앞에 괄호닫고
# -> 왜 뭐가 도대체 뭐때문에 틀린걸까?
# '''
# s = list(map(str,input()))
# result_str = ""
# flag = 0 # flag = 1이면 열린괄호가 있다는 말이다.
# for i in s:
#     if i == '-':
#         if flag == 0:
#             result_str += i
#             result_str += '('
#             flag = 1
#         else:
#             result_str += ')'
#             result_str += i
#             flag = 0
#     else:
#         result_str += i
# if flag == 1:
#     result_str +=')'
# # print(result_str)
# print(eval(result_str))

