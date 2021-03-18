import socket

# IPv4 | tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# assign address, here local
# 2 (()) for tuple
server_socket.bind(('127.0.0.1', 5099))

# how many connections?, here 10
server_socket.listen(10)
print('[+] Listening for connections on 127.0.0.1:5099...')

# incoming requests
while True:
  conn, addr = server_socket.accept()
  print('[+] Got a connection from {}'.format(addr))

  while True:

    # limit on receiving bytes, here 1024 Bytes
    data = conn.recv(1024)
    if(data.decode() == ''): break
    print('[+] Client sent:', data.decode())

    server_data = input('Enter data to send: ')
    conn.send(server_data.encode())

    # Replying to client
    conn.send(b'This is server')
  
  conn.close()