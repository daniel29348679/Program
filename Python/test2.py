# %%
import socket  # 导入 socket 模块

# %%
s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号

s.connect((host, port))
while True:
    mess = input() or "exit"
    s.send(mess.encode("utf-8"))
    if mess == "exit":
        break

s.close()
# %%
print(host)
# %%
