import socket

HOST = '192.168.79.131'  #địa chỉ IP của máy server
PORT = 3000              #Port kết nối

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tạo socket
s.bind((HOST, PORT))
s.listen(2)

while True:
    client, addr = s.accept()
   
    try:
        print('Connected by', addr)
        while True:
            data = client.recv(1024)
            str_data = data.decode("utf8")
            if str_data == "quit":
                break
            print("Client: " + str_data)
 
 
            client.send(bytes("Hello " + str_data, "utf-8"))
               
    finally:
        client.close()

s.close()