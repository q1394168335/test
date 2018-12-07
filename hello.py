from flask import Flask, request 
import socket

app = Flask(__name__)


@app.route('/')
def index():
	# 获取本机计算机名称
	hostname = socket.gethostname()
	# 获取本机ip
	ip = socket.gethostbyname(hostname)
	return  f'hello {ip}.'


if __name__ == '__main__':
	app.run(host='0.0.0.0')
