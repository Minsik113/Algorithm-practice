'''
음식의종류 ~2000개
걸리는시간 ~1000초

'''
# import heapq

# # food_time[i] = i+1번음식이 걸리는시간
# def solution(food_times, k): # k초에는 음식 안먹음. 
#     # 예외처리
#     if sum(food_times) <= k:
#         return -1

#     h = []
#     length = len(food_times)
#     for i in range(length):
#         heapq.heappush(h, (food_times[i],i+1)) # (음식시간,번호)
    
#     sum_value = 0 # 먹기위해 사용하는 시간
#     previous = 0 # 직전에 다 먹은 음식 시간
    
#     # sum_value + (현재의 음식시간 - 이전 음식 시간) * 현재 음식 개수 와 K비교
#     while sum_value + ((h[0][0] - previous)*length) <= k:
#         now = heapq.heappop(h)[0]
#         sum_value += (now - previous) * length
#         length -= 1 # 다 먹은 음식 제외
#         previous = now # 이전 음식 시간 재설정
    
#     # 남은 음식중 몇 번째 음식인지 확인
#     result = sorted(h, key=lambda x:x[1]) # 음식번호로 정렬
#     return result[(k-sum_value)%length][1]
        

