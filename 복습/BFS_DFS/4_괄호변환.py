# # 
# def check(p,u,v,count):
#     # 1번. 빈문자열일경우 빈문자열 반환
#     if len(p) == 0:
#         return p
#     stack = []
#     for i in range(len(p)):
#         stack.append(p[i])
#         u += p[i]
#         count[p[i]] += 1
#         # 2번. 균형잡힌 괄호문자열이면 u,v 분리
#         if count['('] == count[')']: 
#             if i+1 <= len(p)-1: # 범위안에 존재하면
#                 v = p[i+1:]
#         # 이때 u가 올바른 괄호 문자열이라면 v를 
#         if len(stack) >= 2 and p[i] == ')':
#             if p[i] == '(':
#                 count['('] -= 1
#                 count[')'] -= 1
#                 stack.pop()
#                 stack.pop()
                
        
    
# def solution(p):
#     answer = ''
#     u, v = "", ""
#     count['('] = 0 # '(' ')'의 수를 세자.
#     count[')'] = 0
#     result = check(p,u,v,count)
    
#     return answer
