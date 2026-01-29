import socket
import threading

network = {
    "ip": "0.0.0.0",
    "port": 12345,
    "size": 4096
}

def receive_msg(socket):
    while True:
        try:
            data = socket.recv(network.get("size"))
            if not data:
                print("Ngắt kết nối")
                socket.close()
                break
            print(f"\rClient: {data.decode("utf-8")}")
            print("Me: ", end="", flush=True)
        except:
            print("Lỗi kết nối")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((network["ip"], network["port"]))
    server.listen()
    print("=== server open ===")
    client_socket, client_address = server.accept()
    print(f"=> {client_address} connect to server <=")
    print("Gõ 'exit' để ngắt kết nối")

    #Thread nhặn tin hàm receive_msg
    recv_thread = threading.Thread(target=receive_msg, args=(client_socket,))
    recv_thread.daemon = True
    recv_thread.start()
    
    while True:
        msg = input("Me: ")
        if msg.lower() == "exit":
            print("Ngắt kết nối")
            client_socket.close()
            break
        if msg.strip():
            client_socket.sendall(msg.encode("utf-8"))