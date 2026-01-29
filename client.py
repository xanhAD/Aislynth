import socket
import threading

network = {
  "ip": input("Nhap ip connect: "),
  "port": 12345,
  "size": 4096
}

def receive_messages(sock):
  while True:
    try:
      data = sock.recv(network["size"])
      if not data:
        print("Ngat ket noi")
        sock.close()
        break
      print(f"\rServer: {data.decode('utf-8')}")
      print("Me: ", end='', flush=True)
    except Exception as e:
      break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
  try:
    client.connect((network["ip"], network["port"]))
    print("=== server connect ===")
    
    recv_thread = threading.Thread(target = receive_messages, args = (client,))
    recv_thread.daemon = True
    recv_thread.start()
    
    while True:
      msg = input("Me: ")
      if msg.lower() == "exit":
        print("Ngat ket noi")
        client.close()
        break
      if msg.strip():
        client.sendall(msg.encode("utf-8"))
  except Exception as e:
    print(f"Error: {e}")
    