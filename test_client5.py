import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

# 클라이언트 연결 요청
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# 데이터 전송
def handler_tx(client_socket:socket.socket):
    while True:
        send_msg = input("Text: ")
        
        if send_msg.lower() == "exit":
            client_socket.close()
            break
        
        client_socket.sendall(send_msg.encode('utf-8'))
        
# 데이터 수신
def handler_rx(client_socket:socket.socket):
    while True:
        rcvd_msg = client_socket.recv(1024).decode('utf-8')
        if not rcvd_msg:
            break
        
        print(f"Received msg: {rcvd_msg}")

# thread target -> bind -> join
thread_tx = threading.Thread(target=handler_tx, args=(client_socket))
thread_rx = threading.Thread(target=handler_rx, args=(client_socket))

thread_tx.start()
thread_rx.start()

thread_tx.join()
thread_rx.join()
