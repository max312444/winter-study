import json

bar = {"name" : "ycjung", "age" : 20, "roomnum" : [404, 501]}

# 파일로 저장 -> 문자열(Text) -> JSON
# bar는 메모리에 존재하는 데이터 -> JSON Serializer
# -> JSON 기반 Text
# with open("text.txt" , "w") as file_handler:
#       json.dump(bar, file_handler)

# serializing
json_str = json.dumps(bar)

print(type(json_str), json_str)

# parsing -> 예외
rcvd_data = json.loads(json_str)

print(rcvd_data.get('phone'))
print(rcvd_data.get('name'))

print(type(rcvd_data['age']), type(rcvd_data['roomnum']), type(rcvd_data['name']))