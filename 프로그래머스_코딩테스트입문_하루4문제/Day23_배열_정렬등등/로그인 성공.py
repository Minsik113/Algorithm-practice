'''
날짜: 2023.01.09
시간복잡도:

문제:

풀이:
23:25~23:28(3분)
단순한 구현
'''
def solution(id_pw, db):
    db_scaling = dict()
    for a,b in db:
        db_scaling[a] = b
    # 1.아이디가 존재할 경우, 
    if id_pw[0] in db_scaling:
        # 1.1 비밀번호 다르면, "wrong pw"출력
        if db_scaling[id_pw[0]] != id_pw[1]:
            return "wrong pw"
        # 1.2 비밀번호 같으면, "login"출력
        return "login"
    else: # 아이디가 존재하지 않을 경우, "fail"출력
        return "fail"
