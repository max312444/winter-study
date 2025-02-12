import socket
import threading

# 주소 받기
HOST = "127.0.0.1"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT)) # 연결 요청 (clinet만 있음)

is_active = [True] # 종료 신호 생성

# 데이터 전송
def handler_tx(client_socket:socket.socket):
    while is_active[0]: # 종료 요청 전까지 반복
        send_msg = input("Text: ") # blocking 함수
        
        if send_msg.lower() == "exit": # 입력한 값이 exit이면 
            client_socket.close() # socket 닫고
            is_active[0] = False # 종료 신호 False로 변경
            break # 반복문 탈출
        
        client_socket.sendall(send_msg.encode('utf-8')) # blocking 함수
        # 입력한 Text를 byte단위로 변경해서 서버로 보내기

# 데이터 수신
def handler_rx(client_socket:socket.socket):
    while is_active[0]: # 종료 요청 전까지 반복
        rcvd_msg = client_socket.recv(1024).decode('utf-8') # blocking 함수
        # 보낸 정보 받기
        if not rcvd_msg: # 보내온 정보가 없다면 
            break # 반복문 탈출
        
        print(f"Received msg: {rcvd_msg}")
        
    is_active[0] = False # 종료 신호 False로 변경

# thread taget -> start -> join
# taget은 위의 함수들 인자값은 client_socket으로
thread_tx = threading.Thread(target=handler_tx, args=(client_socket,))
thread_rx = threading.Thread(target=handler_rx, args=(client_socket,))

thread_rx.start()
thread_tx.start()

thread_rx.join()
thread_tx.join()