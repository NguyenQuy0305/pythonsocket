import socket, ssl

HOST, PORT = "192.168.79.131", 3000

def handle(conn):
    conn.write(b'Nguyen Viet Quy\n')
    print(conn.recv().decode())

def main():
    sock = socket.socket(socket.AF_INET)
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = False
    context.verify_mode=ssl.CERT_NONE
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    conn = context.wrap_socket(sock, server_hostname=HOST)

    try:
        conn.connect((HOST, PORT))
        handle(conn)

    finally:
        conn.close()

if __name__ == '__main__':
    main()