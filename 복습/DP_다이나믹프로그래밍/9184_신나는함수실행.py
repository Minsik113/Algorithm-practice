# # w( %d, %d, %d) = 1 % (a, b, c)
# # print('w(%d, %d, %d) = %d' % (a,b,c,??) )

# dp = dict()

# while True:
#     a, b, c = map(int, input().split())
#     if a == -1 and b == -1 and c == -1:
#         break
#     strings = '(a, b, c)'
#     w(a, b, c)
    
#     def w(a, b, c):
#         if a <= 0 or b <= 0 or c <= 0:
#             print('w(%d, %d, %d) = 1' % (a,b,c))
#         elif a > 20 or b > 20 or c > 20:
#             print(w(20,20,20))
        
#         elif a < b and b < c:
#             print( w(a,b,c-1) + w(a,b-1+c-1) - w(a,b-1,c))
#         else:
            
    

