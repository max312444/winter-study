import socket
import threading

# 서버의 IP 주소 및 포트 설정
HOST = "127.0.0.1"  # 로컬호스트 (localhost) 주소
PORT = 12345  # 사용할 포트 번호

is_active = [True]  # 종료 신호 (리스트를 사용하여 다중 스레드 환경에서 값 변경 가능하도록 함)

# 데이터 전송 함수 (클라이언트에게 메시지를 전송)
def handler_tx(client_socket: socket.socket):
    """
    클라이언트에게 데이터를 전송하는 함수
    - 사용자가 'exit'을 입력하면 종료
    - 입력받은 데이터를 UTF-8로 인코딩하여 전송
    """
    while is_active[0]:  # 종료 요청이 있기 전까지 반복
        send_msg = input("Test: ")  # 사용자 입력값 받음
        
        if send_msg.lower() == "exit":  # 사용자가 'exit' 입력 시 
            client_socket.close()  # 소켓 닫기 (데이터 송신 종료)
            is_active[0] = False  # 종료 신호 False로 변경
            break  # 반복문 탈출
        
        client_socket.sendall(send_msg.encode('utf-8'))  # 입력한 값을 UTF-8로 인코딩하여 전송

# 데이터 수신 함수 (클라이언트로부터 메시지를 받음)
def handler_rx(client_socket: socket.socket):
    """
    클라이언트로부터 데이터를 수신하는 함수
    - 클라이언트가 데이터를 보내면 UTF-8로 디코딩하여 출력
    - 클라이언트가 연결을 종료하면 반복문 탈출
    """
    while is_active[0]:  # 종료 요청이 있기 전까지 반복
        rcvd_msg = client_socket.recv(1024).decode('utf-8')  # 수신한 데이터를 UTF-8로 디코딩
        
        if not rcvd_msg:  # 클라이언트가 연결을 종료하면 빈 메시지가 들어오므로 종료
            break  # 반복문 탈출
        
        print(f"Received msg: {rcvd_msg}")  # 수신한 메시지 출력
        
    is_active[0] = False  # 수신 스레드 종료 후 종료 신호 False로 변경

# 소켓 생성 (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# - `AF_INET`: IPv4 주소 체계를 사용
# - `SOCK_STREAM`: TCP (신뢰성 있는 연결 기반 통신) 방식 사용

# 서버의 IP 주소와 포트 바인딩 (연결 대기 준비)
server_socket.bind((HOST, PORT))

# 클라이언트의 접속 요청을 기다림 (최대 1개 동시 접속 허용)
server_socket.listen(1)

print(f"[Listen] {HOST}, {PORT}")

# 클라이언트 연결 요청 수락
client_socket, client_addr = server_socket.accept()  # 클라이언트의 연결 요청을 허용
print(f"[Connected] 클라이언트 {client_addr} 접속")

# 송신(TX) 및 수신(RX) 스레드 생성
# - target: 실행할 함수 지정 (handler_tx, handler_rx)
# - args: 해당 함수에 전달할 인자 (client_socket)
thread_tx = threading.Thread(target=handler_tx, args=(client_socket,))
thread_rx = threading.Thread(target=handler_rx, args=(client_socket,))

# 두 스레드 실행 (병렬로 데이터 송수신 수행)
thread_tx.start()  # 송신 스레드 시작
thread_rx.start()  # 수신 스레드 시작

# 두 스레드가 종료될 때까지 대기
thread_rx.join()  # RX 스레드 종료 대기
thread_tx.join()  # TX 스레드 종료 대기
