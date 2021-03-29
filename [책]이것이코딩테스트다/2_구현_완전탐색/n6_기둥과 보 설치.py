# # 모르겟다.
# '''
# 삭제시)
# 기둥 = 조건에 만족안하면 무시
# 보 = 설치한 구조몰이 조건에 만족안하면 무시
# -> array[x][y] = 0
# 0은 없음 1이면 기둥, 2이면 보끝, 3이면 보중간
# '''
# def possible(answer):
#     for x, y, stuff in answer:
#         if stuff == 0: # 설치된 것이 '기둥'이라면
#             # '바닥 위' or '보의 한쪽 끝부분 위' or '다른 기둥 위' 가능
#             if y == 0 or [x-1,y,1] in answer or [x,y-1,0] in answer or [x,y,1] in answer:
#                 continue
#             # 안되면 불가능
#             return False 
#         elif stuff == 1: # 설치된 것이 '보'
#             # '한쪽 끝부분이 기둥 위' or '양쪽 끝부분이 다른 보와 동시에 연결'
#             # 보는 오른쪽으로 연결하니까 (x,y-1) or (x+1,y-1)이 기둥인지 봐야함
#             if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
#                 continue
#             # 안되면 불가능
#             return False
#     return True
            
    
# def solution(n, build_frame):
#     answer = []
#     for frame in build_frame: # stuff = 0기둥 . 1보
#         x, y, stuff, operator = frame
#         if operator == 0: # 삭제하는 경우
#             answer.remove([x,y,stuff]) # 일단 삭제 해본 뒤 검사
#             if not possible(answer): # 구조물유지가 불가능하면 다시설치
#                 answer.append([x,y,stuff])
#         if operator == 1: # 설치하는경우
#             answer.append([x,y,stuff])
#             if not possible(answer):
#                 answer.remove([x,y,stuff])
    
#     return sorted(answer)