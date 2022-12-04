'''
날짜: 2022.12.04
시간복잡도: O(NlogN)

문제:
풀이:
숫자의 index를 파악하면됨
내림차순 정렬했을때 몇번째에 있는지 파악해라.
->줄세우고 원본이랑 비교

'''
def solution(emergency):
    answer = [0]*len(emergency)

    arr = []
    for idx, i in enumerate(emergency): # O(N)
        arr.append([i, idx])
    arr_sorted = sorted(arr, key=lambda x:-x[0]) # O(NlogN)
    # 해당위치에 순서 넣기
    for i in range(len(emergency)): # O(N)
        answer[arr_sorted[i][1]] = i+1
    
    return answer