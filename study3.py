try:
    print("pos")
    print(1/0) # 주석 처리 on/off에 따른 결과 값 확인
    print("bar")
    kin()
    
    raise IndexError("인덱스 예외 발생")
except ValueError: 
    print("ValueError 예외 발생")
except IndexError as e:
    print(f"예외 발생: {e}")
except NameError as e: 
    print(f"예외 발생: {e}")
except ZeroDivisionError:
    print("ZeroDivisionError 예외 발생")

print(f"결과 : 0")
