import socket
import threading

# 함수 생성
def handler_client(client_socket, client_addr):
    while True:
        rcvd_data = client_socket.recv(1024).decode('utf-8')
        
        if not rcvd_data:
            print("[Closed from client]")
            break
        
        print(f"[Rcva data ({client_addr})]: {rcvd_data}")
        
        client_socket.sendall(rcvd_data.endcode('utf-8'))
    
    client_socket.close()

# 호스트 IP, PORT 주소, 쓰레드 개수 카운트 위한 변수 생성성
HOST = "127.0.0.1"
PORT = 12345
num_of_thread = 0

# 서서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind
server_socket.bind((HOST, PORT))

# listen
server_socket.listen(5)
print(f"Wait for connect....")

while True:
    # accept -> 클라이언트 연결을 수락하고 새로운 소켓 생성
    client_socket, client_addr = server_socket.accept()
    print(f"[Accept] ({client_addr})")
    
    # 새로운 쓰레드 생성
    client_thread = threading.Thread(target=handler_client, agrs=(client_socket, client_addr))
    
    num_of_thread += 1
    print(f"쓰레드 생성 : {num_of_thread}")
    # 생성한 쓰레드 실행
    client_thread.start()
    
server_socket.close()