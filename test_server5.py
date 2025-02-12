import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

client_list = []  # 클라이언트의 socket 정보를 저장하는 리스트
client_list_lock = threading.Lock()  # 레이스 컨디션을 방지하기 위해 Lock 사용

def handler_client(client_socket: socket.socket, client_addr):
    """클라이언트와 메시지를 주고받으며, 연결 종료 시 목록에서 제거하는 함수"""
    try:
        while True:
            rcvd_msg = client_socket.recv(1024).decode('utf-8')  # 클라이언트로부터 메시지를 수신 및 디코딩
            
            if not rcvd_msg:  # 클라이언트가 빈 메시지를 보내거나 연결을 종료하면 반복문 종료
                break
            
            rcvd_msg = f"{client_addr}: {rcvd_msg}"  # 메시지에 보낸 클라이언트의 주소 추가
            
            with client_list_lock:  # 멀티스레드 환경에서 리스트 동기화 (다른 스레드가 동시에 수정하지 못하도록 보호)
                for socket_item in client_list:
                    try:
                        socket_item.sendall(rcvd_msg.encode("utf-8"))  # 클라이언트들에게 받은 메시지를 브로드캐스트
                    except:
                        client_list.remove(socket_item)  # 전송 실패 시 해당 클라이언트를 리스트에서 제거
                        socket_item.close()  # 소켓 닫기
                        
    except Exception as e:
        print(f"[ERROR] Client {client_addr} error: {e}")  # 오류 발생 시 메시지 출력
        
    finally:
        with client_list_lock:  # 클라이언트 연결 종료 시 목록에서 안전하게 제거
            if client_socket in client_list:  # 연결 종료할 클라이언트가 리스트에 존재하는지 확인 후 삭제
                client_list.remove(client_socket)
                
        client_socket.close()  # 클라이언트 소켓 닫기
        print(f"Client {client_addr} disconnected")  # 클라이언트 연결 종료 로그 출력
        
# 서버 소켓 생성 및 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP 사용
server_socket.bind((HOST, PORT))  # 서버 소켓을 지정된 IP와 포트에 바인딩
server_socket.listen(5)  # 최대 5개의 클라이언트 연결 요청을 대기

print(f"Server listening on {HOST}:{PORT}")

try:
    while True:
        print(f"Connected clients: {len(client_list)}")  # 현재 연결된 클라이언트 수 출력
        
        client_socket, client_addr = server_socket.accept()  # 클라이언트의 연결 요청 수락
        print(f"Client connected: {client_addr}")  # 새 클라이언트가 연결되었음을 출력
        
        with client_list_lock:  # 클라이언트 목록에 안전하게 추가
            client_list.append(client_socket)

        # 클라이언트별 개별 스레드 생성 및 실행 (백그라운드 실행을 위해 daemon=True 설정)
        client_thread = threading.Thread(target=handler_client, args=(client_socket, client_addr), daemon=True)
        client_thread.start()
        
except KeyboardInterrupt:  # 서버가 Ctrl+C로 종료될 경우
    print("\n[INFO] Server shutting down...")  # 서버 종료 메시지 출력
    
finally:
    with client_list_lock:  # 서버 종료 시 모든 클라이언트의 연결을 안전하게 종료
        for client_socket in client_list:
            client_socket.close()  # 모든 클라이언트 소켓 닫기
            
    server_socket.close()  # 서버 소켓 닫기
    print("[INFO] Server closed")  # 서버가 정상적으로 종료되었음을 알림
