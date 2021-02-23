import json

# 사전 자료형(dict) 데이터 선언
user = {
    "id": "Jessy"
    , "password": "123456"
    , "age": 25
    , "hobby": ["watching movie","watching TV"]
}

# JSON 데이터로 변환하여 파일로 저장
with open("uesr.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent=4)

# -> '복습'폴더에 .json 생성됨