# 1. 사용자 입력 오류
# 숫자를 입력받아야 하지만, 문자를 입력할 경우 발생하는 오류
num = int(input("1 또는 2를 입력하세요: "))

try:
    if num == 1:
        raise ValueError # raise 예외를 발생시킨다!
    else:
        raise NameError
    print("bar")
# result = int(num) * 2 # ValueError 발생 가능
except ValueError: # 예외 처리 구문
    print("ValueError 예외 발생")
except NameError: # 예외 처리 구문
    print("NameError 예외 발생")

print(f"결과 : 0")