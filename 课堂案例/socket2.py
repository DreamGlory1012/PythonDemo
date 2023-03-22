"""
    Author: AubreyChen
    Time: 2023/3/21 10:37
    File: socket2.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
import socket
import threading

# 设置服务器地址和端口
SERVER_HOST = 'localhost'
SERVER_PORT = 8000

# 创建套接字并连接到服务器
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# 处理服务器消息的线程
# 创建处理服务器消息的线程并启动
def handle_server():
    while True:
        try:
            # 接收服务器发送的消息
            message = client_socket.recv(1024)
            if message:
                print('服务器发送消息：%s' % message.decode('utf-8'))
            else:
                # 断开与服务器的连接
                client_socket.close()
                print('与服务器断开连接。')
                break
        except:
            # 断开与服务器的连接
            client_socket.close()
            print('与服务器异常断开连接。')
            break

server_thread = threading.Thread(target=handle_server)
server_thread.start()

# 发送消息给服务器的函数
def send_message():
    while True:
        message = input('请输入要发送的消息（输入 q 退出）：')
        if message == 'q':
            # 关闭客户端套接字
            client_socket.close()
            break
        # 发送消息给服务器
        client_socket.send(message.encode('utf-8'))

send_thread = threading.Thread(target=send_message)
send_thread.start()
