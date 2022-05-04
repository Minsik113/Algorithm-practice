##########################################
# regex? import re이용해서도푸네?

##########################################
##########################################
# 해쉬이용 (출제자 의도)
def solution(phone_book):
    answer = True
    hash_map = dict()
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number # 한글자 씩 더함
            # temp가 사전에 있고 찾고자하는것과 동일한게 아니라면
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
##########################################
##########################################
# sort해서풀자 -> 어케푼거지 ㅋㅋ
def solution(phoneBook):
    phoneBook.sort(key=lambda x: len(x))
    for a in range(len(phoneBook)):
        for b in range(a+1, len(phoneBook)):
            if phoneBook[b][:len(phoneBook[a])] == phoneBook[a]:
                return False
    return True

##########################################
##########################################
# permutations이용
# '''
# 모든 경우를 비교 permutatation 2개씩해서 비교 (a,b)
#     if len(a) > len(b)면 넘어감
#     else:
#     a길이만큼 b랑 비교해보고 같으면 False. 더안봐도됨. 종료
# '''
# from itertools import combinations

# def solution(phone_book):
#     # 예외처리
#     if len(phone_book) == 1:
#         return False
    
#     flag = False
#     for i in combinations(phone_book,2):
#         v1, v2 = i[0], i[1]
#         if len(v1) > len(v2): # 길이 작은게 v1로 가게 만든다.
#             v1, v2 = v2, v1
#         if v1 == v2[:len(v1)]: # 같은게 존재한다면
#             flag = True
#             break
        
#     # 모든경우 다봤는데 flag ==False라면 같은건 없음
#     if not flag:
#         return True
#     else:
#         return False