'''
1. num1 num2의 최소 공배수 구한다.
2. 차이만큼 분자에더함. 
3. 나눠지는지 체크.
'''
# 최대 공약수
def GCD(x, y):
    while y > 0:
        x,y = y, x%y
    return x
# 최소 공배수
def LCM(x, y):
    result = (x*y) // GCD(x,y)
    return result
def solution(denum1, num1, denum2, num2):
    answer = []
    
    # 1.분모의 최소공배수 구하기
    t = LCM(num1, num2)
    a = denum1 * (t // num1) # 분자에 a만큼 곱해야함
    b = denum2 * (t // num2)
    de = a + b # de:분자 t:분모
    # print(de,t)
    
    # 2.기약분수인지 확인
    while True:
        temp = GCD(de,t)
        #최대공약수가 1이라면 나옴
        if temp == 1:
            break
        # 아니라면 최대공배수로 약분해준다. 
        else:
            de = de // temp
            t  = t // temp
    # print(de,t)    
    return [de,t]


# 이게 왜 안되는거지?
# def solution(denum1, num1, denum2, num2):
#     answer = []
#     # 1.분모 최소공배수 구하기
#     target = 0
#     for i in range(max(num1, num2), (num1*num2)+1):
#         if i % num1 == 0 and i % num2 ==0:
#             target = i
#             break
#     # 2
#     a = target // num1
#     b = target // num2
#     na = denum1 * a
#     nb = denum2 * b
    
#     de = na+nb
#     n = target
#     # print(de,n)
#     # 분모 분자가 약분이 되는지 알아봐야한다.
#     while True:
#         flag = True
#         for i in range(2, min(de,n)):
#             if de % i == 0 and dn % i == 0: # 나누어지면 나눠야지
#                 de = de // i
#                 n = n // i
#                 flag = False
#                 break
#         if flag:
#             break
#     # print('>>최종: ',de,n)
#     return [de,n]