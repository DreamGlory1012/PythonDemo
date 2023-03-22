"""
    Author: AubreyChen
    Time: 2023/3/21 10:37
    File: socket1.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
import socket
import threading

# 设置服务器地址和端口
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000
# 设置客户端数量上限
CLIENT_LIMIT = 5

# 创建套接字并绑定到地址和端口
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(CLIENT_LIMIT)
print('服务器启动，等待客户端连接...')

# 存储所有已连接的客户端套接字
clients = {}

# 处理客户端连接请求的线程
def handle_client(client_socket, client_address):
    print('客户端 %s:%s 连接成功！' % client_address)
    while True:
        try:
            # 接收客户端发送的消息
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print('客户端 %s:%s 发送消息：%s' % (client_address[0], client_address[1], message))
                # 判断消息是否为回复消息
                if message.startswith('RE:'):
                    # 获取原消息的发送方
                    sender = message.split(':')[1]
                    # 发送回复消息给发送方
                    clients[sender].send(('服务器收到回复消息：%s' % message[3:]).encode('utf-8'))
                else:
                    # 将该客户端套接字存储到字典中
                    clients[client_address] = client_socket
                    # 向所有其他客户端发送该消息
                    for address, sock in clients.items():
                        if address != client_address:
                            sock.send(('客户端 %s:%s 发送消息：%s' % (client_address[0], client_address[1], message)).encode('utf-8'))
            else:
                # 断开客户端连接
                client_socket.close()
                del clients[client_address]
                print('客户端 %s:%s 断开连接。' % client_address)
                break
        except:
            # 断开客户端连接
            client_socket.close()
            del clients[client_address]
            print('客户端 %s:%s 异常断开连接。' % client_address)
            break

# 处理客户端连接的主线程
while True:
    try:
        # 接受客户端连接请求
        client_socket, client_address = server_socket.accept()
        # 创建处理客户端连接的线程
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        # 启动处理客户端连接的线程
        client_thread.start()
    except:
        # 关闭服务器套接字
        server_socket.close()
        break
