'''
음식의종류 ~2000개
걸리는시간 ~1000초
(i초에,음식개수) - ex. (1초걸리는음식,8개) (10초걸리는음식,140개) (1000초,10개)
1. 초당 음식개수 저장
2. k가 음식의 개수보다 적으면 바로 k출력 @@
3. k가 음식의 개수보다 많으면? -> 1초이상인 음식들 다 빼봄  k -= 총음식수
4. k가 2초이상음식수보다 많으면? -> 2초이상인 음식들 다뺴봄 k -= 2초이상음식수
5. 3,4반복
6. k가 i초이상음식수보다 많으면? -> i초이상인 음식들 하나씩 뺴봄.
7. k가 i초이상음식수보다 적으면? -> i초인애들중에서 앞에서 k번째있는거
'''
def solution(food_times, k): # k초에는 음식 안먹음. 
    answer = 0
    if k <= len(food_times):
        if k == len(food_times):
            return 1
        return k+1
    # 걸리는시간 1~1000초니까 각초당 음식이 몇개인지 파악
    food_count = [0] * 1001
    for i in food_times:
        food_count[i] += 1
    # 음식의 종류
    food_type = len(food_times)
    k -= food_type # 전체시간 - 1초이상개수 빼줌.
    num = 2
    # while True:
# https://programmers.co.kr/learn/courses/30/lessons/42891
        
        


