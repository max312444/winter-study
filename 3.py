import socket

def run_client():
    """클라이언트 실행 함수"""
    host = '127.0.0.1'  # 서버 호스트 주소 (localhost)
    port = 12345        # 서버 포트 번호

    # TCP 소켓 생성 (IPv4, TCP 방식)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 지정된 서버 주소와 포트에 연결 요청
    client_socket.connect((host, port))
    print("서버에 연결되었습니다. 메시지를 입력하세요 (종료하려면 'exit' 입력).")

    try:
        while True:
            # 사용자 입력을 받음
            message = input(">>> ")
            if message.lower() == 'exit':  # 'exit' 입력 시 연결 종료
                print("서버와의 연결을 종료합니다.")
                break
            
            # 입력한 메시지를 서버로 전송 (UTF-8 인코딩)
            client_socket.sendall(message.encode('utf-8'))
            
            # 서버로부터 응답을 수신하여 출력 (최대 1024바이트)
            response = client_socket.recv(1024).decode('utf-8') # 이걸 넣어서 서버의 응답을 확인할 수 있다.
            print(f"서버 응답: {response}") # 내가 데이터를 보내야지만 응답을 받을 수 있다. 24번이 실행되야 27번이 실행된다.
    except Exception as e:
        print(f"오류 발생: {e}")  # 예외 발생 시 오류 메시지 출력
    finally:
        client_socket.close()  # 클라이언트 소켓 닫기
        print("클라이언트가 종료되었습니다.")

if __name__ == "__main__":
    run_client()  # 클라이언트 실행