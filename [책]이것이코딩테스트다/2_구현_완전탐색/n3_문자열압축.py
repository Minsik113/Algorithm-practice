# '''
# 문자1개로 압축할 때 ~ 절반크기로 압축할 때
# 제일 짧은 길이로 압축되는 문자열의 길이는?

# 앞부터 정해진 길이로 자르는거라서 그냥 앞부터 묶어서 자르면됨
# 1번. 1~len(s)//2 로 자를 반복문
# 2번.if s[pre:pre+i] == s[pre+i:pre+2i]:
#         count += 1
#     else:
#         pre = s[pre+i:pre+2i]
#         if count != 0:
#             answer += str(count)+s[pre:pre+i]
#             count = 0
#         else:
#             answer += s[pre:pre+i]
# 3번. i번쨰가 끝나면 min_value = min(min_value,len(answer) )
# 4번. min_value 출력
# '''
# def solution(s):
#     min_value = int(1e9)
#     # 예외처리
#     if len(s) == 1:
#         return 1

#     for i in range(1, len(s)//2+1): # 개수가 홀수개일 경우는 맨뒤를 한번 더 봐줘야함
#         pre = s[:i] # 1의길이 ~ 절반의 길이
#         count = 1 # 같은 문자열이 몇 개 인가
#         answer = ""
#         for j in range(i, len(s), i): # i ~ 절반까지 i만큼 뜀
#             # 앞의 문자와 같다
#             if pre == s[j:j+i]:
#                 count += 1
#             # 앞의 문자열과 다르다 - > count
#             else:
#                 # 같은문자열이 없었다
#                 if count == 1:
#                     answer += pre
#                 # 같은 문자열이 있었다 -> count를 더해줌
#                 else:
#                     answer += str(count) + pre
#                     count = 1 # count 갱신
#                 pre = s[j:j+i] # 비교할 문자열 갱신
#         # 남아있는 문자열에 대해서 처리
#         if count >= 2:
#             answer += str(count) + pre
#         else:
#             answer += pre
#         # i문자열로 쭉 보았을 떄, 한번의 비교가 끝났으면 길이 비교
#         min_value = min(min_value, len(answer))
#         # print(answer)
    
#     return min_value

# # '''
# # 10^3 x 10^3 하면 충분
# # 1. 1~len(s) // 2에 대해 압축이 되나 본다.
# # -> len(s)의 반 까지의 길이로 압축해봄.
# # 2. 리스트에 저장한길이중 짧은거 출력
# # '''
# # ##########################################  
# # ##########################################  
# # #
# # def solution(s):
# #     answer = int(1e9)
# #     length = len(s)
# #     if len(s)==1:
# #         return 1
# #     # 1번
# #     count = 1
# #     for plus in range(1,length//2+1): # 길이1 ~ 길이절반
# #         temp = ''
# #         for i in range(0,length,plus): # 
# #             # 1. 같으면 이어서본다.
# #             if s[i:i+plus] == s[i+plus:i+plus*2]: 
# #                 # print(plus,'일때',s[i:i+plus])
# #                 count += 1
# #             # 2. 같지않으면 그대로 문자열에 추가
# #             else: 
# #                 if count == 1: # 겹치는게 없음
# #                     temp += s[i:i+plus]
# #                 else: # 겹치는 횟수 만큼
# #                     temp += str(count) + s[i:i+plus]
# #                     count = 1
                    
# #         # print(temp)
# #         answer = min(answer, len(temp))
    
# #     return answer
# # ##########################################  
# # ##########################################  
# # #
# # def solution(s):
# #     answer = len(s)
# #     for step in range(1, len(s)//2 + 1):
# #         strings = ""
# #         prev = s[0:step] # 앞에서 step만큼의 문자열 추출
# #         count = 1
# #         for j in range(step,len(s),step):
# #             # 1번 같은 문자열이라면
# #             if s[j:j+step] == prev:
# #                 count += 1
# #             # 2번 다른 문자열일 경우
# #             else:
# #                 strings += str(count) + prev if count >= 2 else prev
# #                 prev = s[j:j+step] # 상태초기화
# #                 count = 1
# #         # 남아있는 문자열 정리
# #         strings += str(count) + prev if count >= 2 else prev
# #         # 만들어지는 문자열중 짧은것이 정답
# #         answer = min(answer, len(strings))
    
# #     return answer