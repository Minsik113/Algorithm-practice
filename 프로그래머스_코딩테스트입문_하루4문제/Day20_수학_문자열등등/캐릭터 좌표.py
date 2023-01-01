'''
날짜: 2022.12.27 -> 2023.01.01
시간복잡도:

문제:
풀이:
23:59~00:13
l r u d
1.좌우로 얼마나 움직였는가
2.상하로 얼마나 움직였는가
'''
def solution(keyinput, board):
    answer = []
    lr = 0
    ud = 0
    
    tx = board[0] // 2 # x범위 [-tx, tx]
    ty = board[1] // 2 # y범위 [-ty, ty]
    for i in keyinput:
        if i =="":
            break
        elif i[0]=='l':
            if lr != -tx:
                lr -= 1
        elif i[0] == 'r':
            if lr != tx:
                lr += 1
        elif i[0] == 'd':
            if ud != -ty:
                ud -= 1
        else:
            if ud != ty:
                ud += 1
        # print(lr,ud)
        
    return [lr,ud]