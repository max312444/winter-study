import socket

# 소켓 생성 (TCP or UDP, IP 주소 버전: v3 or v6)
# TCP : socket.SOCK_STREAM
# UDP : socket.SOCK_DGRAM

sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind (ip 주소, port 주소)
sever_socket.bind(('127.0.0.1', 5500))

# listen(큐의 개수)
sever_socket.listen(5)
print(f"listen on 127.0.0.1:5500")

# accept(), -> 사용자로부터 연결 요청을 받았을 때 -> 새로운 소켓 생성
# 클라이언트 -> connect()
client_socket, client_addr = sever_socket.accept() # 연결 요청시 새로운 소켓을 자동으로 생성 후 반환한다.
# 프로그램 블락 -> 사용자의 연결 요청이 올 때 까지.

print(f"[client ip address] : {client_addr}")

# 클라이언트로부터 메시지를 수신 
# 현재 연결된 소켓으로 부터 데이터를 받아옴 () 안은 몇 바이트씩 읽어오는 지에 대한 크기이다.
while True:
    rcvd_data = client_socket.recv(1024) .decode('utf-8')

    print(f"type of rcvd_data : {type(rcvd_data)}")

# 동기 함수인가 비동기 함수인가? - 동기 함수이다. 데이터 받아올 때까지 대기
# 받은 데이터의 자료형은? - byte형이다. 비트 단위를 byte단위로 묶어서 데이터를 전송한다.
# 왜냐하면 우리가 주고받는 데이터들은 전부 0,1 로 이루어져 있는데 자료형에 따라 비트 단위가 다르기 때문에
# 어떤 자료형인지 알 수 없다. 하지만 byte 단위로 묶어서 이게 정수인지 문자인지 확인 가능하게 보낸다.
# 수신한 메시지를 클라이언트로 전송
