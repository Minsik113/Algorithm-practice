'''
JSON 목킹 사이트 이용
목킹(Moking)
: 어떠한 기능이 있는 것처럼 흉내내어 구현한 것을 의미
-> 단순히 REST API와 JSON형식을 익히기에는 번거로우므로 목킹사이트 이용함
https://jsonplaceholder.typicode.com/


'''
##########################################
##########################################
# 문제1 
# 번호순서대로 사용자의 이름만 리스트에 담자.
import requests

# 1. Rest api경로에 접속해서 응답(Response) 데이터 받아오기
target = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url=target)

# 2. 응답(Response) 데이터가 JSON형식이므로 파이썬객체로 변환
data = response.json()

# 3. 모든 사용자(user) 정보를 확인하며 이름 정보만 삽입
name_list = []
for user in data:
    name_list.append(user["name"])
print(name_list)