
import socket

HOST = "127.0.0.1"
PORT = 12345

# socket 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect()
client_socket.connect((HOST, PORT))

while True:
    # 사용자로부터 데이터 입력
    send_msg = input("Input text: ")
    
    if send_msg.lower() == "exit":
        break

    # 입려된 데이터를 서버로 전송
    client_socket.sendall(send_msg.encode("utf-8"))

    # 서버로부터 수신한 데이터를 출력
    rcvd_msg = client_socket.recv(1024).decode('utf-8')

    print(f"[Client rcvd data]: {rcvd_msg}")

client_socket.close()
print("클라이언트 종료")