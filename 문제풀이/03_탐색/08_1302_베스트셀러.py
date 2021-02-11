# 1/19
# 문제 난이도: Silver 4
# 문제 유형: 탐색
# 추천 풀이 시간: 20분

# 가장 많이 등장한 문자열을 출력하는 문제
# 등장 횟수를 세는 무제니까 dict() 이용.

######################  ######################
x = int(input())
data = dict()

for _ in range(x):
    name = input()
    if name not in data:
        data[name] = 1
    else:
        data[name] += 1

target = max(data.values())

s_data = sorted(data.items(),key=lambda x: x[0])

for book, name in s_data:
    if name == target:
        print(book)
        break
    
######################  ######################
# 동빈나

n = int(input())
books = dict() # 책이름,팔린 수

for _ in range(n): 
    name = input()
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

#print(books)
target = max(books.values())
data = []
#print(target)

for book, number in books.items():
    if number == target:
        data.append(book)
print(sorted(data)[0])

        