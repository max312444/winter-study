try:
    print("1")
    
    raise IndexError # 주석 처리

    raise KeyError

    print("2")
    
    print("3")
except Exception: # 이게 더 상위 레벨이기 때문에 이게 실행된다.
    print("3.1")
except LookupError: # Index와 Key의 상위 계층인 Lookup으로 에러 처리
    print("3.5")
    
print("7")