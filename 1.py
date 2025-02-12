import socket

def run_server():
    """싱글 스레드 TCP 서버 실행 함수"""
    host = '127.0.0.1'  # 서버 호스트 주소 (localhost)
    port = 12345        # 사용할 포트 번호

    # TCP 소켓 생성 (IPv4, TCP 방식)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 서버 소켓에 IP와 포트 바인딩 - 포트 번호를 받아옴(운영체제가 관리). 이걸 client 포드번호로 지정
    server_socket.bind((host, port))
    
    # 클라이언트의 접속을 기다림 (최대 5개 대기 가능) - 연결 대기 상태
    server_socket.listen(5)
    
    print(f"서버가 {host}:{port}에서 대기 중입니다...")
    
    try:
        while True:
            # 클라이언트의 연결 요청 수락 (하나씩 처리)
            client_socket, client_address = server_socket.accept() # 연결 요청 오기 전까지 멈추고 소켓을 새로 하나 더 만든다
            # 다른 사용자의 연결 요청을 받기위해 새로운 소켓을 만든다. 그래서 클라이언트의 소켓을 받고 새로운 소켓을 만드는 것이다.
            print(f"클라이언트 연결됨: {client_address}")
            
            try:
                while True:
                    # 클라이언트로부터 메시지 수신 (최대 1024바이트)
                    message = client_socket.recv(1024).decode('utf-8')
                    if not message:  # 메시지가 없으면 연결 종료
                        print(f"클라이언트 연결 종료: {client_address}")
                        break
                    print(f"[{client_address}] {message}")  # 받은 메시지 출력
                    
                    # 에코(받은 메시지를 다시 클라이언트에게 전송)
                    client_socket.sendall(f"서버 응답: {message}".encode('utf-8'))
            except Exception as e:
                print(f"클라이언트 처리 중 오류 발생: {e}")
            finally:
                client_socket.close()  # 클라이언트 소켓 종료
    except KeyboardInterrupt:
        print("서버가 종료되었습니다.")
    finally:
        server_socket.close()  # 서버 소켓 닫기

if __name__ == "__main__":
    run_server()  # 서버 실행
