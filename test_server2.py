# test_server2.py

import socket
import threading

def handler_client(client_socket, client_addr):
    # send, receive 진행
    # echo server   
    while True: # 반복문 종료 조건 : 클라이언트가 close() 함수를 호출했을 때때. 이때 빈문자열을 출력한다.
        # blocking 함수. 클라이언트로부터 수신이 오면 해제
        rcvd_data = client_socket.recv(1024).decode('utf-8') 

        if not rcvd_data: # 데이터가 없으면 반복문 종료
            print("[Closed from client]")
            break

        print(f"[Rcvd data ({client_addr})]: {rcvd_data}")
        
        # 수신된 데이터를 전송
        client_socket.sendall(rcvd_data.encode('utf-8'))
        
    client_socket.close()

HOST = "127.0.0.1" # 서버의 IP 주소 -> 문자형
PORT = 12345 # 포트 주소 -> 정수형
num_of_threads = 0

# socket 생성
sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind
sever_socket.bind((HOST, PORT))

# listen
sever_socket.listen(5)
# 여기에서 연결 요청을 "대기열(큐)"에 저장하는 것임!
print(f"Waiting for connect...")

while True:
    # accept -> 클라이언트 연결을 수락하고 새로운 소켓을 생성
    client_socket, client_addr = sever_socket.accept()
    # 연결된 클라이언트의 IP와 PORT 정보를 가져온다.
    print(f"[Accept] ({client_addr})")

    # 새로운 쓰레드 생성
    client_thread = threading.Thread(target=handler_client, args=(client_socket, client_addr))
    
    num_of_threads += 1
    print(f"쓰레드 생성 : {num_of_threads}")
    # 생성된 쓰레드 실행
    client_thread.start()
    

# 이 코드가 실행되면 모든 연결이 종료된다!
sever_socket.close() 