'''
1. -id마다 불린 횟수 저장하는 dict()
2. 띄어쓰기로 구분해서 a b (신고자 신고당한유저)
3. -id마다 누구신고했는지 저장하는 dict() 생성
4. 1전체를 보면서 k와 비교
5. 3전체 보면서 answr채우기
'''
def solution(id_list, report, k):
    answer = dict()       # 정답
    dict_count = dict()   # id마다 신고당한 횟수
    dict_report = dict()  # id를 신고한 id들
    for name in id_list:
        answer[name] = 0
        dict_count[name] = 0 
        dict_report[name] = []
        
    for names in report:
        a, b = names.split()
        bool_check = True
        for name in dict_report[b]:
            if a in name:
                bool_check = False # b를 신고한 a가 이미 존재함
                break
        if bool_check:
            dict_count[b] += 1       # b신고당했으니 1추가
            dict_report[b].append(a) # b를 신고한 a 추가
    for a,b in dict_count.items():
        if b >= k: # a가 k번넘게 신고당했으면 신고한애들 count증가
            for zz in dict_report[a]:
                answer[zz] += 1
    
    print(dict_count)
    print(dict_report)
    return list(answer.values())