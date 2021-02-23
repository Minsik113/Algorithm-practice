'''
JSON데이터는 키-값 쌍으로 이루어진 데이터 객체를 저장하고 있다.
'''
import json

# 사전 자료형(dict) 데이터 선언
user = {
    "id": "G-Dragon"
    , "password": "20201010"
    , "age": 27
    , "hobby": ["programming", "play game(lol)"]
}

# 인코딩: 파이썬 변수를 JSON객체로 변환(띄어쓰기 4칸)
json_data = json.dumps(user, indent=4)
print(json_data)

# 디코딩: JSON객체를 파이썬 변수로 변환
data = json.loads(json_data)
print(data)
