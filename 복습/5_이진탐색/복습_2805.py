'''
절단기 범위 0~양의정수

나무를 필요한 만큼만 가져간다. 많으면 길이 줄여서 다시자름.
적으면 길이 늘려서 다시자름.
M의 나무를 가져갈때 절단기높이의 최대값은 ??

'''
n, m = map(int, input().split()) # 나무수, 가져가고자하는 길이m
data = list(map(int, input().split()))

# 절단은 0 ~ 제일 긴 나무의 높이 까지 절단할 수 있다.
start = 0
end = max(data)
result = 0
while start <= end:
    mid = (start + end) // 2
    count = 0 # mid로 잘랐을때 나무의 개수

    # 나무 베어본다
    for i in range(len(data)):
        if data[i] - mid > 0: # 잘리면 count에 더한다
            count += data[i] - mid
            if count >= m: # 더많이 잘랐으면 나와서 줄임
                break
    # 많이 잘렸으면 더 높게 잘라본다
    if count >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)